# DataGen Overview

DataGen is a Python-based data generation framework that produces synthetic forecasting and supply-chain data for use in commercial planning tools such **Oracle Fusion SCM**. It supports an initial bulk load, incremental (delta) data by time period, and consolidation of historical and new data. Final outputs can be formatted for upload into a target system (e.g. FBDI for Oracle Fusion).

This document describes the three main entry points and the role of the FBDI-composition scripts.

---

## 1. DataGen 1010 — Initial (Bulk) Data Generation

**Script:** `DataGen_1010_Main_DataGen_Initial.py`

**Purpose:** Generate a **large initial dataset** suitable for loading into a commercial forecasting or SCM tool (e.g. Oracle Fusion SCM). This is the “seed” data that represents a baseline of organizations, items, customers, and time-series (orders, forecast, inventory, etc.).

**Operation:**

1. **Configuration**  
   Loads application parameters from the config file via `DataGen_1110_Load_config_main` (paths, calendar, item/customer hierarchies, trends, etc.).

2. **Master data (when source type is Random)**  
   - **1210** — Initial **organizations** (e.g. legal entities, planning orgs).  
   - **1220** — Initial **items** (hierarchy + item IDs with configurable prefixes and counts).  
   - **1230** — Initial **customers** (location/ship-to hierarchy and IDs).  

   Outputs go to `*_base` files (e.g. `ITEMS_base.csv`, `CUSTOMERS_base.csv`).

3. **Matrix and core data**  
   - **1240** — Initial **matrix** of ITEM-to-CUSTOMER combinations (which items are sold at which locations), with attributes (status, lifecycle, trends).  
   - **1250** — Initial **coredata** (orders, forecast, inventory, safety stock, etc.) per period/item/location.  
   - **1260** — **Post-process** coredata (e.g. rolling averages, derived fields) and write the post-processed file.

4. **FBDI for target system**  
   - **1290** — **Compose FBDI Booking History**: reads the (base) coredata and produces an **FBDI-formatted CSV** ready for upload into Oracle Fusion SCM (e.g. Demand Management / planning). Output is written to the path configured for the main FBDI booking file.

**Outputs:**  
Base CSV files (organizations, items, customers, matrix, coredata) and the initial **FBDI Booking History** file for the target system. These base files are also the foundation for later delta runs.

---

## 2. DataGen 1012 — Delta (Incremental) Data Generation

**Script:** `DataGen_1012_Main_DataGen_Delta.py`

**Purpose:** Add **incremental, consistent data** on a **per-time-period** basis. Each run produces a small delta (new items, new customers, new matrix rows, new coredata for the new period) and merges it with existing “merged” data to form updated `*_merged_new` datasets. This supports ongoing simulation of a planning environment (e.g. weekly or monthly deltas).

**Operation:**

1. **Prerequisites**  
   - Checks that all required **base** files exist (items, customers, organizations, matrix). If any are missing, the script exits with an error.  
   - Ensures **merged** files exist: if a merged file is missing, it is created by copying the corresponding base file.

2. **Delta sequence (13xx)**  
   - **1310** — Organizations delta (if used; often fixed orgs).  
   - **1320** — **Items delta**: reads existing merged items, determines the next available ID per prefix, and generates a small number of new items (configurable min/max per period).  
   - **1330** — **Customers delta**: same idea for customers (next ID per prefix from merged, then new customers).  
   - **1340** — **Matrix delta**: new ITEM–CUSTOMER combinations, ensuring each (Item, Location) key is unique across merged and delta.  
   - **1345** — **Increment period** (e.g. advance week/month in the period tracker) and **merge** base + delta + existing merged into `*_merged_new` (items, customers, matrix).  
   - **1350** — **Coredata delta** for the new period.  
   - **1355** — **Prep coredata** (as needed for downstream).  
   - **1360** — **Post-process** coredata (e.g. rolling averages).  
   - **1390** — **Compose FBDI Booking History** from the **merged_new** coredata; writes to the “new” FBDI booking path (e.g. for the latest delta run).

**Outputs:**  
Delta CSV files, updated `*_merged_new` files (items, customers, organizations, matrix, coredata), an updated period tracker, and an **FBDI Booking History (new)** file based on the merged_new coredata. The existing `*_merged` files are left unchanged until consolidation (1014).

---

## 3. DataGen 1014 — Approve and Consolidate Delta

**Script:** `DataGen_1014_Main_Approve_and_consolidate_delta.py`

**Purpose:** **Combine** the older, larger “merged” datasets with the recently produced incremental data (`*_merged_new`) so that the consolidated result becomes the new canonical “merged” set for the next delta cycle and for any exports (e.g. 1290) that use merged data.

**Operation:**

1. **Prompt**  
   Asks: *“Approve consolidation of new delta records?”*  
   Proceeds only if the user answers **Y** or **Yes** (case insensitive). Otherwise the script exits without changing any files.

2. **Backup**  
   Copies the current `*_merged` and `*_merged_new` files (items, customers, organizations, matrix) into the configured backup directory, each with a **timestamp prefix** (e.g. `YYYYMMDD_HHMMSS_ITEMS_merged.csv`). If any backup fails, the script reports an error and stops; no deletes or renames are performed.

3. **Replace merged with consolidated data**  
   - Deletes the current `*_merged` files (items, customers, organizations, matrix).  
   - Renames each `*_merged_new` file to the corresponding `*_merged` name.  

   So the content that was “merged_new” (base + previous merged + latest delta) becomes the new “merged” dataset.

4. **Error handling**  
   If backup fails, or if any delete/rename fails, the script logs a clear message and exits so that the user can fix issues without losing data. On success, the consolidated data is in place for the next delta run and for any process that reads from merged files.

**When to use:**  
After one or more delta runs (1012), when you are satisfied with the incremental data and want to “promote” it into the main merged set. After 1014, the next 1012 run will use this consolidated set as its merged input and add further deltas on top.

---

## 4. Preparing Data for the Target System — 1290 and 1390

**Purpose:** Turn internal coredata (and related structures) into a **format suitable for uploading** into the target system (e.g. Oracle Fusion SCM). In this project, that format is **FBDI (File-Based Data Import)** for Booking History.

### DataGen_1290_Compose_FBDI_Booking_History

- **Input:** COREDATA **base** (the initial coredata produced by 1010, post-processed).  
- **Output:** A single FBDI-formatted CSV (e.g. Booking History) configured in the config file (e.g. `PATH_FBDI_BOOKING`).  
- **Use case:** After running **1010 Initial**, use 1290 to produce the **initial** FBDI file for loading into Oracle Fusion SCM (or similar).

### DataGen_1390_Compose_FBDI_Booking_History

- **Input:** COREDATA **merged_new** (the combined base + merged + latest delta coredata produced at the end of a 1012 run).  
- **Output:** A “new” FBDI Booking History file (e.g. `PATH_FBDI_BOOKING_NEW`).  
- **Use case:** After running **1012 Delta**, use 1390 to produce the **latest** FBDI file that includes all consolidated history plus the new period. This file can be used for incremental or full refresh loads in the target system. After **1014 Approve and consolidate**, the merged coredata becomes the new baseline; the next 1012 run will again produce merged_new and 1390 will again output from that.

Both scripts map internal fields (period, item, location, measures, etc.) to the FBDI column layout expected by Oracle Fusion (e.g. Technical Name, plan name, measure name, product/location/time levels, value, flags).

---

## 5. Acquiring Data from Oracle Fusion via REST — 1410 and 1420

### 5.1 1410 — Acquire ITEMs

**Script:** `DataGen_1410_Acquire_ITEMs_from_Oracle_via_REST.py`

**Purpose:** Call an **Oracle Fusion SCM** REST API to **retrieve a list of ITEMs** from a designated Fusion environment (e.g. DEV, TEST, PROD). The result is written to a CSV file for use as a source of item master data (e.g. for Custom source type or validation).

**Operation:**

1. **Configuration**  
   Uses parameters loaded by `DataGen_1110_Load_config_main` from the **FUSION_SCM** and **PATHS** sections: `v_parm_fusion_name`, `v_parm_fusion_env`, `v_parm_fusion_url`, `v_parm_fusion_username`, `v_parm_fusion_password`, and `v_parm_path_items_from_source` (output file path).

2. **REST API**  
   - Endpoint (defined in the script): `/fscmRestApi/resources/11.13.18.05/itemsLOV`.  
   - Full URL: `v_parm_fusion_url` + endpoint; request uses Basic Auth and `Content-Type: application/json`.

3. **Pagination**  
   - Requests are made with `limit` and `offset` query parameters (e.g. limit=500).  
   - A **while-loop** continues until the response indicates no more records (`hasMore` is false or `totalResults`/`totalItems` is zero).  
   - Each response’s HTTP status and JSON body are stored in arrays for traceability.

4. **Output**  
   - All items (and their attributes) from every response are written to **`v_parm_path_items_from_source`** as a **quote-delimited, comma-separated CSV**.  
   - The file is created or overwritten; the output directory is created if needed.

**Use case:** Pull current item master data from Oracle Fusion SCM for use as a Custom item source, for comparison with generated data, or as input to downstream scripts. Can be run standalone or as part of a larger pipeline.

### 5.2 1420 — Acquire CUSTOMERs

**Script:** `DataGen_1420_Acquire_CUSTOMERs_from_Oracle_via_REST.py`

**Purpose:** Call an **Oracle Fusion SCM** REST API to **retrieve a list of CUSTOMERs** (shipping customers LOV) from a designated Fusion environment. The result is written to a CSV file for use as a source of customer data (e.g. for Custom source type or validation).

**Operation:**

1. **Configuration**  
   Uses the same **FUSION_SCM** parameters as 1410, and **`v_parm_path_customers_from_source`** (output file path) from the PATHS section.

2. **REST API**  
   - Endpoint (defined in the script): `/fscmRestApi/resources/11.13.18.05/shippingCustomersLOV`.  
   - Full URL and auth behave the same as 1410.

3. **Pagination and output**  
   - Same pagination (limit/offset, hasMore, totalResults/totalItems) and CSV format as 1410.  
   - All customers (and their attributes) are written to **`v_parm_path_customers_from_source`** as quote-delimited, comma-separated CSV.

**Use case:** Pull current shipping customer data from Oracle Fusion SCM for use as a Custom customer source or for validation. Can be run standalone or as part of a larger pipeline.

---

## Typical Workflows

| Goal | Steps |
|------|--------|
| **Initial load for a new planning instance** | Run **1010** (Initial) → use **1290** output as the FBDI file to load into Oracle Fusion SCM. |
| **Add one or more time periods of new data** | Run **1012** (Delta) one or more times → use **1390** output (FBDI new) for upload. |
| **Lock in deltas as the new baseline** | Run **1014** (Approve and consolidate) after 1012 when ready → then continue with further 1012 runs; 1290 can be used on the consolidated merged coredata if you need a full “post-consolidation” FBDI export. |
| **Acquire item list from Oracle Fusion** | Run **1410** (Acquire ITEMs from Oracle via REST) → use `v_parm_path_items_from_source` CSV as item source or for validation. |
| **Acquire customer list from Oracle Fusion** | Run **1420** (Acquire CUSTOMERs from Oracle via REST) → use `v_parm_path_customers_from_source` CSV as customer source or for validation. |

Configuration (paths, hierarchies, period type, delta counts, FBDI paths, Fusion REST settings, etc.) is centralized in the main config file loaded by **DataGen_1110_Load_config_main**.
