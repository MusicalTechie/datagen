# Changelog

Notable changes to the DataGen application. See **`TODO.md`** for the current action list and **`python_datagen/IMPROVEMENT_RECOMMENDATIONS.md`** for detailed recommendations and status.

---

## Recent changes (post-analysis)

### Config and loader review (2026-02)

After manual updates to `config_main.ini` and `DataGen_1110_Load_config_main.py`, the following was reviewed and corrected:

- **config_main.ini** – No structural errors. Sections LOG, APP, PATHS, DATABASE, COMPANY, DATAGEN are present and consistent. PATHS include `PATH_FBDI_BOOKING` and `PATH_FBDI_SHIPMENT`; DATAGEN includes all expected keys. Note: `DG_ITEM_HIER_NAMES` defines five level names (including DemandType) while `DG_ITEM_HIER_LVLS` is 4; this may be intentional for a future fifth level.
- **DataGen_1110_Load_config_main.py** – Bug fixes and log corrections:
  - **PATH_ITEMS_DELTA_CSTM** – Was assigned to `v_parm_path_items_delta`, overwriting the non-custom delta path. Now correctly assigned to `v_parm_path_items_delta_cstm`.
  - **Log messages** – Several `logging.debug()` calls were logging the wrong variable (e.g. base path when loading _CSTM path). Corrected for: PATH_ITEMS_BASE_CSTM, PATH_ITEMS_MERGED_CSTM, PATH_ORGANIZATIONS_BASE_CSTM, PATH_ORGANIZATIONS_DELTA_CSTM, PATH_CUSTOMERS_BASE_CSTM, PATH_CUSTOMERS_DELTA_CSTM, PATH_CUSTOMERS_MERGED_CSTM, PATH_FBDI_BOOKING, PATH_FBDI_SHIPMENT, and DATAGEN keys DG_LEGAL_ENTITY, DG_BUSINESS_UNIT, DG_ORG_MASTER, DG_ORG_PLANNING.
  - **DG_ORG_PLANNING** – Loaded value was stored in `v_parm_dg_date_org_planning` (typo). Renamed to `v_parm_dg_org_planning` for consistency; no other code referenced the old name.

### Bug fixes

- **Sleep import** – `DataGen_1240_Generate_coredata_initial.py` and `DataGen_1250_PostProcess_coredata.py` now use `from time import sleep` so `sleep(1)` does not raise `NameError`.
- **PostProcess FIFO tail** – When writing the last rows from the FIFO queue, each row now uses its own content for placeholder replacement (previously all used row_05). The FIFO was then refactored to a list with a single flush loop.
- **Main script working directory** – After `os.chdir(v_appDir)`, the script now sets `v_cwd = os.getcwd()` so the “application working directory” message is correct.
- **Config loader** – PATH log messages now print the correct variable for each path. The incomplete variable `v_parm_db_` was renamed to `v_parm_db_type`.
- **1240 default trend branch** – The fallback “default to a line” branch now uses `v_current_trend_line_y` and line-based capacity instead of the previously unset `v_current_trend_seasonal_y`.
- **1240 future variance** – Future-period forecast variance now uses `v_parm_dg_dmd_fc_variance` from config instead of a hardcoded `.30`.
- **Typo** – “Intermitent” corrected to “Intermittent” in `DataGen_1230_Generate_matrix_initial.py`.

### Portability and configuration

- **Paths from script location** – The main script (`DataGen_1010_Main_DataGen_Initial.py`) and the config loader (`DataGen_1110_Load_config_main.py`) no longer use hardcoded user paths. Project root and config file path are derived from `__file__` (parent of `python_datagen` and `data_config/config_main.ini` respectively).
- **Logging** – The config loader uses the `logging` module; level is set from `FLAG_LOGLEVEL` in config (DEBUG when &gt; 0, else INFO). Conditional parameter prints were replaced with `logging.debug(...)`.
- **1240 loglevel** – The hardcoded `v_parm_flag_loglevel = 1` override in `DataGen_1240_Generate_coredata_initial.py` was removed so the script respects config.

### Structure and maintainability

- **Shared hierarchy CSV** – New module **`DataGen_shared_hierarchy_csv.py`** with `generate_hierarchy_csv(hier_names_json, hier_lvls, list_json, output_path)`. **`DataGen_1210_Generate_items_initial.py`** and **`DataGen_1220_Generate_locations_initial.py`** now call this instead of duplicating logic.
- **Trend type in 1240** – Trend selection uses `v_list_dmd_trends[i]["TrendName"]` and equality checks (e.g. `== "Slope01"`) instead of `str(...)` and `.find(...)`.
- **PostProcess FIFO** – The six row variables and five copy-paste tail blocks in `DataGen_1250_PostProcess_coredata.py` were replaced by a list `v_fifo_rows` and a single loop to flush remaining rows.

### Tests and documentation

- **Tests** – Added **`python_datagen/tests/`** with:
  - `test_config_load.py` – Config path resolution and presence of expected sections.
  - `test_shared_hierarchy_csv.py` – Shared hierarchy CSV generator (file creation and row count).
  Run with: `pip install pytest` then `python -m pytest python_datagen/tests -v` from the project root.
- **README.md** – Updated to describe portable paths, shared hierarchy module, logging, and project layout (including how to run tests).
- **IMPROVEMENT_RECOMMENDATIONS.md** – Added “Status of recommendations” and updated the priority list with done/deferred/open.
- **TODO.md** – P0, P1, and P3 items updated and done list extended.

### Deferred

- **Deduplicate history/future in 1240** – Extracting a single “build one period row” and reusing it in both history and future loops was deferred as a larger refactor.

---

*For feature roadmap and future work, see **README.md** (Roadmap) and **TODO.md**.*
