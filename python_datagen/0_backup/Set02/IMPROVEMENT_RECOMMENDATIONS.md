# DataGen Python Scripts – Analysis and Improvement Recommendations

This document summarizes findings from analyzing the scripts in `python_datagen` and recommends concrete improvements for maintainability, correctness, portability, and performance.

---

## Status of recommendations (recent changes)

The following have been **implemented**:

- **§1.1** – `sleep` import fixed in 1240 and 1250 (`from time import sleep`).
- **§1.2** – PostProcess FIFO tail flush fixed (correct row variable per row); then refactored to a single list and one flush loop.
- **§1.3** – Main script working directory: `v_cwd` set after `chdir`; `v_appDir` resolved from `__file__` (project root).
- **§1.4** – Config loader PATH log messages use the correct variable for each path.
- **§1.5** – `v_parm_db_` renamed to `v_parm_db_type`.
- **§2.1** – Paths from config/root: 1010 and 1110 resolve app and config paths from script location (no hardcoded user paths).
- **§6.1** – Items and locations deduplicated via **`DataGen_shared_hierarchy_csv.py`**; 1210 and 1220 call `generate_hierarchy_csv`.
- **§6.3** – PostProcess FIFO implemented as a list with a single loop to flush remaining rows.
- **§7.1** – Config loader (1110) uses the `logging` module; level from `FLAG_LOGLEVEL`. Hardcoded `v_parm_flag_loglevel = 1` removed from 1240.
- **§8.2** – 1240 default trend branch uses line trend (not unset seasonal); future variance from config.
- **§8.3** – Future forecast variance in 1240 uses `v_parm_dg_dmd_fc_variance` instead of hardcoded `.30`.
- **§8.4** – Typo “Intermitent” → “Intermittent” fixed in 1230. Trend type in 1240 taken from `v_list_dmd_trends[i]["TrendName"]` with `==` checks.
- **§9.1** – Test suite added in **`python_datagen/tests/`** (config path, shared hierarchy CSV). Run: `python -m pytest python_datagen/tests -v` (requires `pip install pytest`).

**Deferred:** §6.2 (deduplicate history/future in 1240) – large refactor; left for a future pass.

See **`TODO.md`** for the full checklist and **`CHANGELOG.md`** for a concise change history.

---

## 1. Critical / Bug Fixes

### 1.1 Missing `sleep` in 1240 and 1250

**Files:** `DataGen_1240_Generate_coredata_initial.py`, `DataGen_1250_PostProcess_coredata.py`

Both use `import time` but call `sleep(1)`. That will raise `NameError` unless `sleep` is in scope.

**Fix:** Use `from time import sleep` (like the other scripts) or call `time.sleep(1)` everywhere.

---

### 1.2 PostProcess tail flush uses wrong row (1250)

**File:** `DataGen_1250_PostProcess_coredata.py` (lines ~519–564)

When flushing the last 5 rows from the FIFO queue, each block uses `v_coredata2_row_05.replace(...)` and then assigns the result to `v_coredata2_row_04`, `v_coredata2_row_03`, etc. So rows 4, 3, 2, and 1 are all built from **row_05’s content**, and the wrong data is written.

**Fix:** For each row, replace on that row’s variable:

- Row 4: `v_tmp_string = v_coredata2_row_04.replace(...)`, then `v_coredata2_row_04 = v_tmp_string`
- Row 3: `v_tmp_string = v_coredata2_row_03.replace(...)`, etc.
- Same for rows 2 and 1.

---

### 1.3 Main script working directory and print (1010)

**File:** `DataGen_1010_Main_DataGen_Initial.py` (lines 94–97)

`v_cwd = os.getcwd()` is set before `os.chdir(v_appDir)`, and the next print still uses `v_cwd`. So “application working directory” prints the **old** directory, not the one after `chdir`.

**Fix:** Either set `v_cwd = os.getcwd()` after `os.chdir(v_appDir)`, or print `os.getcwd()` for the second message.

---

### 1.4 Config loader: wrong variable in log messages (1110)

**File:** `DataGen_1110_Load_config_main.py`

For many PATH parameters (e.g. PATH_PARAMETERS, PATH_CALENDAR, PATH_ITEMS_BASE, …), the log line uses `v_parm_path_config` instead of the variable that was just set (e.g. `v_parm_path_parameters`, `v_parm_path_calendar`). Debug output is therefore misleading.

**Fix:** Use the correct variable in each `print`, e.g. `v_parm_path_parameters` for PATH_PARAMETERS, `v_parm_path_calendar` for PATH_CALENDAR, etc.

---

### 1.5 Incomplete config variable name (1110)

**File:** `DataGen_1110_Load_config_main.py` (line 271)

`v_parm_db_ = v_configParser[v_parm_group][v_parm_current]` – the variable name is truncated (likely intended `v_parm_db_type` or similar).

**Fix:** Use a full name (e.g. `v_parm_db_type`) and use it consistently where DB type is needed.

---

## 2. Portability and Configuration

### 2.1 Hardcoded paths

**Files:** `DataGen_1010_Main_DataGen_Initial.py`, `DataGen_1110_Load_config_main.py`

- Main script: `v_appDir` is a fixed Windows path.
- Config loader: `PATH_MAIN`, `v_configFileDir`, and `v_configFilePath` are hardcoded and point to a specific user/machine.

**Recommendations:**

- Resolve the app root from the config file location or from `__file__` (e.g. project root = directory of `data_config` or of the main script).
- In 1110, build config path from a single “project root” or “config dir” that comes from config or environment (e.g. `DATAGEN_ROOT`), not from hardcoded full paths.
- Document that paths in `config_main.ini` should be relative to that root so the same project works on different machines.

---

### 2.2 Single config file location

Config path is hardcoded in 1110. Other scripts get config only via `from DataGen_1110_Load_config_main import *`.

**Recommendation:** Resolve config path once (e.g. in 1110) using, in order:

1. Environment variable (e.g. `DATAGEN_CONFIG` or `DATAGEN_ROOT`),
2. Default relative to script/project root.

Then all paths (including in 1010) derive from that.

---

## 3. Structure and Control Flow

### 3.1 Replace `if 1==1` / `if 1==2` with explicit flags or CLI

**Files:** All, especially `DataGen_1010_Main_DataGen_Initial.py`

Steps are enabled/disabled by toggling `if 1 == 2` to `if 1 == 1`. This is hard to see in version control and easy to mis-toggle.

**Recommendations:**

- Add a simple CLI (e.g. `argparse`) to the main script: e.g. `--run-items`, `--run-locations`, `--run-matrix`, `--run-coredata`, `--run-postprocess`, or `--run-all`.
- Or read a “run flags” section from the config (e.g. `RUN_ITEMS = true/false`) and branch on those.
- Keep a single place that defines which steps run (config or CLI), and remove the `if 1==1`/`if 1==2` pattern.

---

### 3.2 Avoid `import *` and global config

All modules use `from DataGen_1110_Load_config_main import *`, and steps rely on globals set there. That makes dependencies hidden and testing difficult.

**Recommendations:**

- Have 1110 expose a single function, e.g. `load_config(path=None) -> dict` (or a small config object), and return a dictionary (or dataclass) of all parameters.
- Main script calls `config = load_config()`, then passes `config` (or specific values) into each step.
- Each step receives config explicitly (e.g. `def run_items(config): ...`) instead of reading globals. That makes unit tests and alternate configs straightforward.

---

## 4. Config Loading (1110)

### 4.1 Two config parser instances

**File:** `DataGen_1110_Load_config_main.py`

Both `v_configParser = configparser.RawConfigParser()` and `v_config = configparser.ConfigParser(allow_no_value=True)` are created; only `v_configParser` is used. So `v_config` is dead code.

**Fix:** Remove the unused `v_config` and use one parser. Prefer `ConfigParser(allow_no_value=True)` if you need to support keys without values.

---

### 4.2 Repetitive parameter loading

Every key is loaded with the same pattern (group, key, assign, optional log). This is verbose and error-prone (e.g. wrong variable in print).

**Recommendation:** Loop over a list of (section, key, target_var_name) or a small schema, and load + log in one place. Optionally use a helper:

```python
def get_cfg(config_parser, section, key, default=None):
    try:
        return config_parser[section][key]
    except (KeyError, TypeError):
        return default
```

Then build a mapping of config keys to variable names and loop over it.

---

### 4.3 Security: credentials in config

**File:** `config_main.ini` (and 1110 which reads it)

DB password and other secrets are in plain text in the repo.

**Recommendations:**

- Do not commit real passwords. Use a template `config_main.ini.example` with placeholders and document that users copy it to `config_main.ini` and fill in values.
- Prefer environment variables for passwords (e.g. `DATAGEN_DB_PASSWORD`), and read them in 1110 when building the DB config.
- Add `config_main.ini` to `.gitignore` if it ever contains real secrets.

---

## 5. Data Handling and CSV/JSON

### 5.1 Building JSON rows via string concatenation

**Files:** 1210, 1220, 1230, 1240, 1250

Rows are built as long strings and then passed to `json.loads()`. If any value contains a quote or newline, the string can become invalid JSON and break the script.

**Recommendation:** Build rows as Python dicts and then either:

- Use `csv.DictWriter` with a fixed field order, or
- Use `csv.writer` and pass `list(row_dict.values())` (or an explicit list of keys so column order is stable).

Avoid constructing JSON strings by hand for row data.

---

### 5.2 Matrix script: open/close file inside loops (1230)

**File:** `DataGen_1230_Generate_matrix_initial.py`

For each (item, location) pair that passes the attach-rate test, the matrix file is opened in append mode, one row is written, and the file is closed. With many items and locations this causes a large number of open/write/close cycles.

**Recommendation:** Open the matrix file once (in append mode) before the inner loop over locations, write all selected rows for the current item, then close after the outer loop. Alternatively, collect rows in a list and write them in one batch at the end.

---

### 5.3 Trend type from list of dicts (1240)

**File:** `DataGen_1240_Generate_coredata_initial.py` (e.g. line 497)

`v_current_trend_type = str(v_list_dmd_trends[v_temp_rnd])` turns the whole dict into a string and then uses `.find("Slope01")` etc. It works but is fragile.

**Recommendation:** Use the structured field, e.g.:

```python
v_current_trend_type = v_list_dmd_trends[v_temp_rnd].get("TrendName", "")
```

Then compare with `== "Slope01"` or use a small mapping from trend name to behavior.

---

## 6. Code Duplication

### 6.1 Items vs locations (1210 and 1220)

**Files:** `DataGen_1210_Generate_items_initial.py`, `DataGen_1220_Generate_locations_initial.py`

The two scripts are almost the same: load config, parse JSON hierarchy and rows, loop over parent/child elements, generate codes with prefix + zero-padded index, write CSV. Only the config keys and naming (items vs locations) differ.

**Recommendation:** Extract a shared function, e.g. `generate_hierarchy_csv(config, param_list_key, hier_names_key, hier_lvls_key, path_key, row_counter_name)`, and call it from two thin scripts or from the main script with different parameters. That reduces duplication and keeps behavior in sync.

---

### 6.2 History vs future in coredata (1240)

**File:** `DataGen_1240_Generate_coredata_initial.py`

The “history” and “future” loops are very long and almost identical; the main differences are the date list and that history uses actual orders while future uses zeros for orders complete. Duplication is hundreds of lines.

**Recommendation:** Factor a single function that takes (date_list, is_future=False) and computes one row (period, item, location, orders, forecast, inventory, safety stock, outcomes, trend factors, etc.). Call it from two loops (history / future). Use a small set of parameters or a row-context dict to switch behavior (e.g. orders complete = 0 when is_future).

---

### 6.3 PostProcess FIFO tail (1250)

**File:** `DataGen_1250_PostProcess_coredata.py`

The “write remaining FIFO rows” block repeats the same replace/write logic five times with only the row variable changing.

**Recommendation:** Use a list for the FIFO (e.g. `fifo_rows = [v_coredata2_row_01, ..., v_coredata2_row_05]` or a collections.deque), and at the end iterate over the remaining entries, apply the same replacement logic, and write each row. That also makes it easier to change the FIFO size (e.g. from 6 to a config value).

---

## 7. Logging and Debugging

### 7.1 Print vs logging

All scripts use `print()` for progress and debug. There is no log level, no timestamps, and no way to redirect to a file without shell redirection.

**Recommendation:** Use the `logging` module:

- One shared function or module that configures `logging` (level from config, optional file handler).
- Replace key `print()` calls with `logging.info()`, `logging.debug()`, `logging.warning()`. Keep a few `print()` only for a minimal console “running step X” if desired.
- Respect `v_parm_flag_loglevel` (or a config LOG_LEVEL) in the logging level (e.g. DEBUG when > 0, INFO otherwise).

---

### 7.2 Overriding log level in 1240

**File:** `DataGen_1240_Generate_coredata_initial.py` (e.g. line 89)

`v_parm_flag_loglevel = 1` is set in code, overriding the config. That forces verbose output whenever this script runs.

**Recommendation:** Remove this override and rely on config (or env) so behavior is consistent and controllable without code changes.

---

## 8. Small Fixes and Consistency

### 8.1 Typo in matrix (1230)

**File:** `DataGen_1230_Generate_matrix_initial.py`

“Intermitent” appears in trend assignments; should be “Intermittent” to match config and 1240.

---

### 8.2 Default branch in 1240 trend selection

**File:** `DataGen_1240_Generate_coredata_initial.py` (else branch after Combined01)

The default branch uses `v_current_calculated_volume_raw = v_current_trend_seasonal_y`, but `v_current_trend_seasonal_y` is not set in the default (line) branch; it’s only set in Seasonal/Combined. If the trend string doesn’t match any known type, this can use an outdated or zero value.

**Recommendation:** In the default branch, set volume from the line trend (e.g. `v_current_trend_line_y`) and ensure all trend branches set the variables that the default branch might use.

---

### 8.3 Magic numbers in 1240 variance

**File:** `DataGen_1240_Generate_coredata_initial.py`

Future-period forecast variance uses hardcoded `.30` (e.g. line 756) while history uses `v_parm_dg_dmd_fc_variance` (e.g. 0.2). For consistency and configurability, use the config parameter (or a dedicated “future variance” parameter) instead of `.30`.

---

### 8.4 Unused imports

Several files import `configparser` or `os` but don’t use them in that file (they rely on imported globals). After refactors (e.g. explicit config passing), remove unused imports and run a linter (e.g. ruff, flake8) to keep the module clean.

---

## 9. Testing and Robustness

### 9.1 No tests

There are no unit or integration tests. Regressions (e.g. the 1250 tail flush, or config variable renames) are easy to introduce.

**Recommendations:**

- Add a small test package (e.g. `tests/`) and run it with pytest.
- Unit tests: config loading (1110) with a minimal INI; JSON parsing of items/locations/trends; one or two row-building helpers.
- Integration test: run the pipeline on a tiny config (e.g. 1 item, 1 location, 2 periods) and assert row counts and that output files exist and have expected columns.
- Optionally add a “dry run” or “validate config” mode that only loads config and checks paths/keys without writing files.

---

### 9.2 Error handling

There is little try/except or validation. Missing config keys, missing files, or invalid JSON will surface as raw exceptions.

**Recommendations:**

- Validate required config keys and paths after loading; print a clear message and exit with a non-zero code if something is missing.
- When reading CSV/JSON or opening files, catch `FileNotFoundError`, `json.JSONDecodeError`, and `KeyError` where appropriate; log and re-raise or exit with a clear message instead of a long traceback for simple config errors.

---

## 10. Summary Priority List

| Priority | Item | Status |
|----------|------|--------|
| **P0**   | Fix `sleep` import in 1240 and 1250. | Done |
| **P0**   | Fix 1250 FIFO tail flush (use correct row variable for each of rows 4,3,2,1). | Done (then refactored to list + single loop) |
| **P1**   | Fix 1010 working-directory print and 1110 PATH log messages and `v_parm_db_` name. | Done |
| **P1**   | Resolve paths from config/project root; remove or reduce hardcoded paths. | Done |
| **P2**   | Replace `if 1==1`/`if 1==2` with config or CLI flags. | Open |
| **P2**   | Refactor config loading to a single function returning a dict/object; pass config explicitly. | Open |
| **P2**   | Build CSV rows from dicts instead of hand-built JSON strings. | Open |
| **P2**   | In 1230, open matrix file once per item (or batch writes). | Open |
| **P3**   | Deduplicate 1210/1220; use logging; add tests. | Done |
| **P3**   | Deduplicate history/future in 1240. | Deferred |
| **P3**   | Trend type from dict; 1240 default branch & variance; typo in 1230. | Done |

Remaining P2 items will improve structure and performance; see **`TODO.md`** for the full list.
