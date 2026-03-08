# DataGen – Supply Chain Data Generation Application

## Application Purpose

This application generates **random but representative data** that emulates the operation of a manufacturing or distribution company. The data is designed to support supply chain processes with a current focus on:

- **Demand Management** (forecasting)
- **Supply Planning**
- **Replenishment Planning**

Random data—with configurable controls and limits—is used intentionally so that:

- Implementers and developers build for the **general case**
- **Error handling** is more robust
- Solutions are not tuned to a small set of “perfect” data

Random data can also be adjusted to **occasionally insert errors** to test error-handling behavior.

---

## Modes of Operation

The tool supports two operational states:

1. **Initial load** – Generate a large amount of baseline information (e.g., 36 months of history).
2. **Incremental** – Read patterns from previously generated data and extend with **one new period** of data (a day, week, or month), emulating ongoing business operations.

*(Incremental per-period generation is on the roadmap; see Roadmap below.)*

---

## Data Types Generated

| Data Type   | Status   | Description |
|------------|----------|-------------|
| **Calendar** | Exists   | Daily, weekly, and/or monthly time buckets. Manually prepared in Excel to match end-client or project needs. |
| **Item**     | Exists   | Products to be purchased, manufactured, and/or distributed. |
| **Location** | Exists   | Sites where products are assigned (manufactured, delivered). |
| **Customer** | Pending  | End-clients that receive finished goods (FG). |
| **Matrix**   | Exists   | Pairs items with locations in a random but representative way (item–location combinations). |
| **Core Data**| Exists   | Random but representative order history (bookings, shipments) and related transactional/planning data. |

---

## Technology

- **Language:** Python  
- **Libraries:** Standard and third-party Python libraries (e.g., `configparser`, `pandas`, `openpyxl`, `xlrd` as needed)  
- **Input/Output:** CSV and Excel files  

---

## Method and Script Flow

### 1. Calendar (manual)

A **calendar** is prepared manually in Excel by the user. It reflects the specific end-client or project (e.g., fiscal vs. Gregorian, period type, date ranges).

### 2. Main entry and configuration

**`DataGen_1010_Main_DataGen_Initial.py`**

- Main Python script that orchestrates all subsequent steps.
- Resolves the **project root** from the script’s location (no hardcoded paths); sets working directory there.
- Loads configuration from **`config_main.ini`** in the **`data_config`** subdirectory (path also resolved from script location).
- Uses **`if 1 == 1`** to run a sub-procedure and **`if 1 == 2`** to skip it. This pattern allows variables loaded in `DataGen_1110_Load_config_main.py` to remain in scope (global) across imports.
- Calls sub-procedures via **`from ModuleName import *`** (not subprocess), so shared config variables stay available.

### 3. Configuration loader

**`DataGen_1110_Load_config_main.py`**

- Resolves **`config_main.ini`** from the project root (parent of `python_datagen`), so the same repo works on any machine.
- Reads the config and populates global variables used by the rest of the pipeline.
- Uses the **`logging`** module; verbosity is controlled by **`FLAG_LOGLEVEL`** in the `[LOG]` section (DEBUG when &gt; 0, else INFO).

### 4. Master data generation

**`DataGen_1210_Generate_items_initial.py`** and **`DataGen_1220_Generate_locations_initial.py`**

- Generate **items** and **locations** following naming patterns and hierarchy defined in config.
- Item/location counts vary within min/max limits from the config.
- Both use the shared **`DataGen_shared_hierarchy_csv.py`** module (`generate_hierarchy_csv`) to avoid duplicated logic.
- *Roadmap:* Option to use an alternate, manually provided item or location file as source.

### 5. Matrix (item–location combinations)

**`DataGen_1230_Generate_matrix_initial.py`**

- Combines **items** with **locations** using an **attachment rate** (probability) from the config.
- Not every item is held, manufactured, or delivered at every location; only a percentage (attachment rate) of pairings are created.
- Each pairing is a **combination** (item–location).
- For each combination, attributes (e.g., forecasting type) are set and remain **static** so that future period generation can continue the same pattern.

### 6. Core transactional data

**`DataGen_1240_Generate_coredata_initial.py`**

- For each **item–location combination**, reads attributes and generates the required number of **periods** of data (e.g., orders, forecasts, inventory).
- *Roadmap:* Add incremental per-period generation to augment existing data files.

### 7. Post-processing

**`DataGen_1250_PostProcess_coredata.py`**

- Processes core data to include **calculations that span periods** (e.g., rolling averages across rows/periods).
- Output is suitable for import into:
  - Local Excel for review, or  
  - Target applications such as **Oracle Fusion Cloud SCM**, **Snowflake**, **SAP**, etc.

---

## Configuration (`config_main.ini`)

The **`data_config/config_main.ini`** file drives behavior, including:

- Paths (config, parameters, calendar, base/delta/merged results for items, locations, matrix, coredata).
- Calendar type (e.g., FISCAL, GREGORIAN), period type (MONTH, WEEK, DAY), and date ranges.
- Item and location hierarchy definitions and min/max counts (often as JSON structures).
- Matrix attachment rate, demand trends, forecast variance, safety-stock factors.
- Core data and matrix column definitions, production capacity ranges, outcome labels and triggers.

Adjusting these values changes the shape, size, and realism of the generated data.

---

## Roadmap

- **Per-period data generation** – Same Python scripts with parameters or dedicated script variants to add one period (day/week/month) to existing data.
- **Python dashboards** – Replace or complement manually updated Excel dashboards with Python-generated views.
- **Web and mobile** – Integrate with a web-based (e.g., AWS) application framework serving iOS and Android.
- **Oracle Fusion integration** – Extract from and load to Oracle Fusion (REST, SOAP, or Oracle FBDI files).
- **Access control** – Sys-admin vs. end-user roles and login.
- **Application lifecycle** – Clean enable/disable of the application with appropriate messaging (e.g., when a client contract ends).

---

## Project layout and running

- **Project root** – Resolved at runtime from the main script’s location (parent of `python_datagen`). No hardcoded user paths in the main or config-loader scripts.
- **Config** – `data_config/config_main.ini`. Paths in `[PATHS]` (e.g. `PATH_MAIN`) can be relative or absolute; the **location of the config file** is always derived from the project layout.
- **Output** – CSV files under paths defined in config (e.g. `data_results/base/`, `data_results/delta/`, `data_results/merged/`).
- **Tests** – In **`python_datagen/tests/`** (config path resolution, shared hierarchy CSV). Run from the project root after `pip install pytest`:
  ```text
  python -m pytest python_datagen/tests -v
  ```
- **Docs** – **`TODO.md`** (action list and done items), **`CHANGELOG.md`** (recent changes), **`python_datagen/IMPROVEMENT_RECOMMENDATIONS.md`** (analysis and status of recommendations).

---

## Summary

DataGen produces configurable, random-but-representative supply chain data (items, locations, matrix, core history and planning data) for demand management, supply planning, and replenishment planning. It runs as a Python pipeline driven by **`config_main.ini`** and a user-defined calendar, with initial bulk generation in place and incremental per-period generation and other enhancements planned on the roadmap. Paths and config file location are resolved from the script directory for portability.
