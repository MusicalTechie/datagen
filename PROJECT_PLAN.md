# DataGen Vision — Project Plan

This document summarizes what has been built, recommended improvements, and the roadmap to merge DataGen with the existing Web and Mobile Application Template so users can run scripts, review data, and submit FBDI to Oracle Fusion SCM from a browser (laptop or mobile).

---

## 1. Current State — What Has Been Created

### 1.1 Base (Initial) Data Creation — Working

The **1010 Initial** pipeline is implemented and operational:

| Component | Status | Description |
|-----------|--------|-------------|
| **Config load (1110)** | Done | Single config file (`config_main.ini`) drives paths, calendar, hierarchies, item/customer definitions, trends, and FBDI output paths. |
| **Organizations (1210)** | Done | Initial organizations (e.g. legal entity, planning org) when source type is Random. |
| **Items (1220)** | Done | Initial items with hierarchy and prefix-based IDs (e.g. `DG_ITEMS` → `MECLC0001`, `MECLA00006`). |
| **Customers (1230)** | Done | Initial customers/ship-to locations with hierarchy and prefix-based IDs. |
| **Matrix (1240)** | Done | ITEM-to-CUSTOMER combinations with status, lifecycle, trends. |
| **Coredata (1250)** | Done | Initial time-series data (orders, forecast, inventory, safety stock, etc.) per period/item/location. |
| **Post-process (1260)** | Done | Rolling averages and derived fields on coredata. |
| **FBDI Booking (1290)** | Done | Composes base coredata into FBDI-formatted CSV for Oracle Fusion SCM. |

**Evidence:** Running `DataGen_1010_Main_DataGen_Initial.py` (with Random source) produces full base CSVs and an FBDI Booking History file suitable for load into a forecasting/SCM tool.

---

### 1.2 Delta (Incremental) Data Creation — Working

The **1012 Delta** pipeline is implemented and operational:

| Component | Status | Description |
|-----------|--------|-------------|
| **Prerequisites (1012)** | Done | Validates base files; creates merged from base when merged is missing. |
| **Organizations delta (1310)** | Done | Delta organizations (often zero; fixed org in use). |
| **Items delta (1320)** | Done | Reads merged items, computes next ID per prefix, generates new items (min/max per period). |
| **Customers delta (1330)** | Done | Same pattern for customers from merged. |
| **Matrix delta (1340)** | Done | New ITEM–CUSTOMER rows; (Item, Location) unique across merged and delta. |
| **Increment & merge (1345)** | Done | Advances period; merges base + delta + merged → `*_merged_new`. |
| **Coredata delta (1350)** | Done | New period coredata. |
| **Prep & post-process (1355, 1360)** | Done | Prep and rolling averages for delta coredata. |
| **FBDI Booking new (1390)** | Done | Composes merged_new coredata into FBDI “new” file. |

**Evidence:** After an initial run (1010), running `DataGen_1012_Main_DataGen_Delta.py` adds a new time period of items, customers, matrix rows, and coredata, and produces updated `*_merged_new` and an FBDI Booking (new) file.

---

### 1.3 Approve and Consolidate — Working

| Component | Status | Description |
|-----------|--------|-------------|
| **1014 Approve and consolidate** | Done | User prompt (Y/Yes) → backup merged & merged_new with timestamp → delete old merged → rename merged_new to merged. Consolidates incremental data into the canonical merged set for the next delta cycle. |

---

### 1.4 Acquire from Oracle Fusion via REST — Working

| Component | Status | Description |
|-----------|--------|-------------|
| **1410 Acquire ITEMs from Oracle via REST** | Done | Calls Oracle Fusion SCM REST API (itemsLOV), paginates with limit/offset until no more records, writes all items and attributes to `v_parm_path_items_from_source` as quote-delimited CSV. Uses config: FUSION_SCM (name, env, URL, username, password) and PATH_ITEMS_FROM_SOURCE. |

**Evidence:** Running `DataGen_1410_Acquire_ITEMs_from_Oracle_via_REST.py` (with valid Fusion config) retrieves item data and writes the CSV; optional test block can force one iteration and display the latest response status and JSON.

---

### 1.5 Supporting Work Completed

- **Shared hierarchy CSV** extended with `start_index_per_prefix` so delta scripts continue ID sequences from merged data.
- **File header consistency:** All Python scripts’ `# = File:` comment matches the actual script filename.
- **Documentation:** `DataGen_Overview.md` (pipelines, FBDI, 1410), `PYTHON_in_AWS.md` (running DataGen in AWS for web/mobile).
- **Version control:** Repo connected to GitHub (MusicalTechie/datagen); local and cloud sync in place.

---

## 2. Recommended Improvements

Prior to or in parallel with web/mobile integration, the following improvements are recommended.

### 2.1 Testing and Validation

| Item | Priority | Description |
|------|----------|-------------|
| **Automated smoke test** | High | Script (e.g. pytest or a small runner) that runs 1010 then 1012 then 1014 in a temp directory and asserts key output files exist and row counts are plausible. |
| **Config validation** | Medium | On load (1110), validate required keys and path format; fail fast with clear messages. |
| **FBDI schema check** | Medium | Optional validation that 1290/1390 output columns match Oracle FBDI expectations (or a known subset). |

### 2.2 Robustness and Operations

| Item | Priority | Description |
|------|----------|-------------|
| **Structured logging** | Medium | Optional JSON or level-based logging to a file for easier parsing and monitoring in a server/API context. |
| **Idempotency / run ID** | Medium | Tag each run (e.g. run ID, timestamp) in logs and optionally in output filenames or metadata for traceability. |
| **Graceful failure** | Medium | Clear exit codes and messages when base files are missing, config is invalid, or a step fails; avoid partial writes where possible. |
| **Secrets** | High | Ensure DB passwords and any API keys are not in config in plain text in repo; use env vars or a secrets manager for production. |

### 2.3 Configuration and Flexibility

| Item | Priority | Description |
|------|----------|-------------|
| **Environment-specific config** | Medium | Support multiple config files or overrides (e.g. DEV vs PROD paths, different FBDI targets). |
| **Delta counts** | Low | Expose or document min/max delta items and customers per period; consider making them overridable via env or API. |

### 2.4 API Readiness (Pre-Integration)

| Item | Priority | Description |
|------|----------|-------------|
| **Single entry point** | High | Thin wrapper or CLI (e.g. `run_initial`, `run_delta`, `run_consolidate`) that can be invoked by an API or job runner without interactive prompts. |
| **1014 non-interactive mode** | High | Optional flag or env var to approve consolidation without prompting (e.g. for automated or API-triggered consolidation). |
| **Output paths** | Medium | Ensure all outputs (CSVs, FBDI) can be written to a configurable directory (or S3) so the web backend can store and expose them. |

### 2.5 Documentation and Onboarding

| Item | Priority | Description |
|------|----------|-------------|
| **README** | Medium | Top-level README with prerequisites, how to run 1010/1012/1014, and pointer to DataGen_Overview.md and config. |
| **Config reference** | Low | Documented list of config sections and keys (or link to config file with inline comments). |

---

## 3. Roadmap — Merge with Web and Mobile Application Template

**Goal:** Integrate DataGen with the existing **Web and Mobile Application Template** (React, JavaScript, PWA) so that users can, from a **browser on a laptop or mobile device**:

- **Initiate scripts** (initial, delta, approve/consolidate).
- **Review data** (inspect generated files, summaries, status).
- **Submit final FBDI data** to an **Oracle Fusion SCM** environment via **REST APIs**.

### 3.1 Target User Experience

- **Menu options** in the app for “DataGen” or “Forecasting Data” (or equivalent).
- **Panels/pages** with:
  - **Buttons/links** to start “Initial load,” “Add delta period,” “Approve & consolidate.”
  - **Tables/list views** to see runs, status, and generated files (e.g. FBDI Booking History).
  - **Actions** to “View” or “Download” CSVs/FBDI and to “Submit to Oracle Fusion” (REST).
- **Responsive layout** so the same flows work on laptop and mobile.

### 3.2 Architecture (High Level)

```
[Browser / PWA]  ←→  [Backend API]  ←→  [DataGen Python]
       ↓                     ↓                    ↓
   Menus, tables,      Start job, status,   1010, 1012, 1014,
   buttons, links      list results,        1290, 1390, 1410
                      submit FBDI                ↓
                            ↓              [Files / S3]
                      [Oracle Fusion
                       SCM REST APIs]
```

- **Backend API:** REST (or GraphQL) service that:
  - Starts DataGen runs (initial, delta, consolidate) as jobs (sync or async).
  - Returns run status and lists of output files (or presigned URLs).
  - Accepts “submit FBDI to Fusion” and calls Oracle Fusion SCM REST APIs with the chosen FBDI payload (or file reference).
- **DataGen:** Runs as described in PYTHON_in_AWS.md (Lambda, Fargate, or EC2); reads config and writes outputs to a shared location (e.g. S3 or EFS) the API can read.
- **Web/Mobile app:** Consumes the backend API; no direct Python execution from the client.

### 3.3 Phased Integration

| Phase | Scope | Deliverables |
|-------|--------|--------------|
| **Phase 1 — Backend for jobs** | Expose DataGen as callable jobs (no UI change yet). | API endpoints: start initial, start delta, start consolidate; get job status; list or get output files (e.g. FBDI). DataGen runs in AWS (or on-prem) as decided. |
| **Phase 2 — UI: initiate and review** | Add DataGen to the Web and Mobile Template. | Menu entry; panels with buttons to start initial/delta/consolidate; tables to show run history and output files; links to view/download FBDI (or CSVs). |
| **Phase 3 — Submit to Oracle Fusion** | End-to-end FBDI submission. | “Submit to Fusion” action; backend calls Oracle Fusion SCM REST APIs (auth, upload FBDI); show success/failure in the app. |
| **Phase 4 — Polish** | Security, roles, and UX. | Auth and authorization for who can run jobs or submit to Fusion; better error messages; optional notifications when a run completes. |

### 3.4 Dependencies and Decisions

- **Oracle Fusion SCM REST:** Confirm which REST APIs and FBDI load mechanism are used (e.g. Import Management, specific bulk load endpoints); implement auth (e.g. OAuth) and error handling.
- **Template repo:** Align with the existing Web and Mobile Application Template’s stack (React version, state management, routing) and add DataGen menu/panels without breaking existing flows.
- **Hosting:** Decide where the backend API and DataGen run (e.g. same AWS account as the template’s backend, or separate); ensure network and IAM allow the API to trigger DataGen and read outputs and to call Oracle Fusion.

---

## 4. Summary

| Area | Status |
|------|--------|
| **Base data creation (1010)** | Working; produces base CSVs and FBDI for initial load. |
| **Delta data creation (1012)** | Working; produces incremental data and merged_new FBDI. |
| **Approve and consolidate (1014)** | Working; promotes merged_new to merged with backup. |
| **FBDI for Oracle Fusion (1290/1390)** | Working; format ready for load; submission via REST is future work. |
| **Acquire ITEMs from Oracle via REST (1410)** | Working; paginated REST call to Fusion itemsLOV; writes CSV to PATH_ITEMS_FROM_SOURCE. |
| **Recommended improvements** | Testing, config validation, non-interactive 1014, API-friendly entry points, secrets management. |
| **Merge with Web/Mobile Template** | Planned; menu-driven UI to initiate scripts, review data, and submit FBDI to Oracle Fusion SCM via REST APIs in phases. |

This project plan will be updated as phases are completed and as the integration with the Web and Mobile Application Template progresses.
