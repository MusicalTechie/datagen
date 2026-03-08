# DataGen – ToDo

Action items and roadmap. See **`CHANGELOG.md`** for recent change details and **`python_datagen/IMPROVEMENT_RECOMMENDATIONS.md`** for detailed rationale and code references.

---

## P0 – Critical (fix first)

- [x] **Fix `sleep` import** – In `DataGen_1240_Generate_coredata_initial.py` and `DataGen_1250_PostProcess_coredata.py` use `from time import sleep` (or `time.sleep(1)`) so `sleep(1)` does not raise `NameError`.
- [x] **Fix PostProcess FIFO tail** – In `DataGen_1250_PostProcess_coredata.py` (~lines 519–564), when flushing the last 5 rows use each row’s own variable for `replace()` (e.g. row 4 → `v_coredata2_row_04`, row 3 → `v_coredata2_row_03`, etc.), not `v_coredata2_row_05` for all.

---

## P1 – High (bugs & portability)

- [x] **Main script working directory** – In `DataGen_1010_Main_DataGen_Initial.py`: after `os.chdir(v_appDir)` set `v_cwd = os.getcwd()` (or print `os.getcwd()`) so the “application working directory” message is correct.
- [x] **Config loader log messages** – In `DataGen_1110_Load_config_main.py`: for each PATH parameter, use the correct variable in the log `print` (e.g. `v_parm_path_parameters` for PATH_PARAMETERS), not `v_parm_path_config`.
- [x] **Config loader DB variable** – In `DataGen_1110_Load_config_main.py`: rename `v_parm_db_` to a full name (e.g. `v_parm_db_type`) and use it consistently.
- [x] **Paths from config/root** – Resolve app and config paths from project root (e.g. relative to script or `data_config`); remove or reduce hardcoded full paths in 1010 and 1110.

---

## P2 – Medium (structure & quality)

- [ ] **Step selection** – Replace `if 1==1` / `if 1==2` in the main script with config flags or CLI (e.g. `argparse`: `--run-items`, `--run-coredata`, `--run-all`).
- [ ] **Config as explicit parameter** – Refactor so `DataGen_1110_Load_config_main` exposes something like `load_config(path=None)` returning a dict/object; pass config into each step instead of `import *` and globals.
- [ ] **Build CSV rows from dicts** – In 1210, 1220, 1230, 1240, 1250: build row data as Python dicts and write via `csv.DictWriter` or `writerow(list(d.values()))`; avoid hand-built JSON strings for rows.
- [ ] **Matrix file I/O** – In `DataGen_1230_Generate_matrix_initial.py`: open the matrix file once per item (or batch) and write all selected rows instead of opening/closing for every item×location pair.
- [ ] **Use single config parser** – In 1110 remove the unused `v_config` and use one parser.
- [ ] **Config credentials** – Use env vars for DB password; add `config_main.ini.example` and document; avoid committing real secrets.

---

## P3 – Lower (maintainability & roadmap)

- [x] **Deduplicate items/locations** – Extract shared logic from 1210 and 1220 into a single hierarchy-to-CSV generator and call it with different config keys.
- [ ] **Deduplicate history/future in 1240** – Factor a single “build one period row” function and call it from both history and future loops (deferred; large refactor).
- [x] **PostProcess FIFO structure** – In 1250 use a list for the FIFO and one loop to flush remaining rows instead of five copy-paste blocks.
- [x] **Logging** – Use `logging` module in 1110; respect config log level; remove hardcoded `v_parm_flag_loglevel = 1` in 1240.
- [x] **Tests** – Add a small test suite in `python_datagen/tests/` (config path, shared hierarchy CSV). Run with `pip install pytest` then `python -m pytest python_datagen/tests -v`.
- [x] **Trend type in 1240** – Use `v_list_dmd_trends[i]["TrendName"]` (or similar) instead of `str(...)` and `.find(...)`.
- [x] **1240 default branch & variance** – In the default trend branch set volume from line trend; use config for future variance instead of hardcoded `.30`.
- [x] **Typo** – In 1230 fix “Intermitent” → “Intermittent”.

---

## Roadmap (features)

- [ ] **Per-period data generation** – Add incremental mode: one new period (day/week/month) appended to existing data (script params or dedicated variant).
- [ ] **Customer file** – Add “Customer” data type (end-clients receiving finished goods); status currently “pending” in README.
- [ ] **Optional item/location sources** – Support alternate, manually provided files for items and locations (roadmap in README).
- [ ] **Python dashboards** – Replace or complement manual Excel dashboards with Python-generated views.
- [ ] **Web & mobile** – Integrate with a web (e.g. AWS) framework and serve iOS/Android.
- [ ] **Oracle Fusion** – Extract from and load to Oracle Fusion (REST, SOAP, or FBDI).
- [ ] **Access control** – Sys-admin vs end-user roles and login.
- [ ] **App lifecycle** – Clean enable/disable with appropriate messaging (e.g. contract end).

---

## Done

*(Move completed items here and add date if desired.)*

- P0: Fix `sleep` import in 1240 and 1250 (use `from time import sleep`).
- P0: Fix PostProcess FIFO tail flush in 1250 (use correct row variable for rows 4, 3, 2, 1).
- P1: Main script working directory: set `v_cwd = os.getcwd()` after `chdir`; resolve `v_appDir` from `__file__` (project root).
- P1: Config loader PATH log messages: each PATH now prints its own variable (e.g. `v_parm_path_parameters`, `v_parm_path_items_base`, …).
- P1: Config loader DB variable: renamed `v_parm_db_` to `v_parm_db_type`.
- P1: Paths from config/root: 1010 uses script-based project root for `v_appDir`; 1110 uses script-based path for `v_configFileDir` and `v_configFilePath` (no hardcoded user paths).
- P3: Typo “Intermitent” → “Intermittent” in 1230.
- P3: Trend type in 1240 from `v_list_dmd_trends[i]["TrendName"]`; default branch uses line trend and config variance.
- P3: Removed hardcoded `v_parm_flag_loglevel = 1` in 1240.
- P3: PostProcess FIFO in 1250 refactored to list + single flush loop.
- P3: Logging in 1110 (basicConfig from FLAG_LOGLEVEL; conditional prints → logging.debug).
- P3: Shared hierarchy generator `DataGen_shared_hierarchy_csv.py`; 1210 and 1220 use it.
- P3: Tests in `python_datagen/tests/` (test_config_load, test_shared_hierarchy_csv). Run: `pip install pytest` then `python -m pytest python_datagen/tests -v`.
