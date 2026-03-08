# ==================================================
# = File:        DataGen_1320_Generate_items_delta.py
# = Purpose:     Generate a small delta of new ITEMs (count between min and max)
# =              and store in v_parm_path_items_delta.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Same type of data generation as initial items but limited by DG_PERIOD_DELTA_ITEMS_MIN/MAX.
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-07
# =  - Updated:
# ==================================================

import csv
import json
import logging
import os
import random
import sys
from time import sleep

v_current_procedure_name = 'Generate ITEMS: DELTA'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
sys.stdout.flush()
sys.stderr.flush()
logging.debug("\n" * 2)
sleep(1)

from DataGen_shared_hierarchy_csv import generate_hierarchy_csv

# --- Build next index per prefix from merged items (Item = fourth column, index 3) ---
v_item_col_idx = 3
v_list_items_config = json.loads(v_parm_dg_items) if isinstance(v_parm_dg_items, str) else v_parm_dg_items
v_prefixes_items = []
for v_elt in v_list_items_config:
    if v_elt.get("ItmPrefix"):
        v_prefixes_items.append(str(v_elt["ItmPrefix"]))
v_prefixes_items = list(dict.fromkeys(v_prefixes_items))  # unique, preserve order
v_max_per_prefix = {p: 0 for p in v_prefixes_items}
if os.path.isfile(v_parm_path_items_merged):
    with open(v_parm_path_items_merged, mode='r', newline='', encoding='utf-8') as f:
        v_reader = csv.reader(f)
        v_rows = []
        for v_i, v_row in enumerate(v_reader):
            if v_i == 0:
                continue
            if len(v_row) > v_item_col_idx:
                v_rows.append(v_row)
    v_rows.sort(key=lambda r: (r[v_item_col_idx] if len(r) > v_item_col_idx else ""))
    for v_row in v_rows:
        v_item_val = v_row[v_item_col_idx].strip()
        for v_p in v_prefixes_items:
            if v_item_val.startswith(v_p):
                v_suffix = v_item_val[len(v_p):].lstrip("0") or "0"
                try:
                    v_num = int(v_suffix)
                    if v_num > v_max_per_prefix.get(v_p, 0):
                        v_max_per_prefix[v_p] = v_num
                except ValueError:
                    pass
                break
v_start_index_per_prefix = {p: v_max_per_prefix.get(p, 0) + 1 for p in v_prefixes_items}

v_min = int(v_parm_dg_period_delta_items_min)
v_max = int(v_parm_dg_period_delta_items_max)
v_n = random.randint(v_min, v_max) if v_max >= v_min else v_min

v_rowCounter_items = 0
if v_n > 0:
    v_output_dir = os.path.dirname(v_parm_path_items_delta)
    if v_output_dir:
        os.makedirs(v_output_dir, exist_ok=True)
    logging.debug("Writing ITEMS delta CSV to: " + str(v_parm_path_items_delta) + " (max " + str(v_n) + " rows)")
    v_rowCounter_items = generate_hierarchy_csv(
        v_parm_dg_item_hier_names,
        v_parm_dg_item_hier_lvls,
        v_parm_dg_items,
        v_parm_path_items_delta,
        max_data_rows=v_n,
        start_index_per_prefix=v_start_index_per_prefix,
    )
else:
    # Write empty file with header only (same structure as base)
    hier_names_list = json.loads(v_parm_dg_item_hier_names) if isinstance(v_parm_dg_item_hier_names, str) else v_parm_dg_item_hier_names
    v_output_dir = os.path.dirname(v_parm_path_items_delta)
    if v_output_dir:
        os.makedirs(v_output_dir, exist_ok=True)
    with open(v_parm_path_items_delta, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for parent_element in hier_names_list:
            writer.writerow(parent_element.values())
    logging.debug("Writing ITEMS delta CSV (0 rows): " + str(v_parm_path_items_delta))

logging.debug("\n" * 2)
logging.debug("Total new ITEM delta rows created: " + str(v_rowCounter_items))
logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
