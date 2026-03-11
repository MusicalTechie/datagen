# ==================================================
# = File:        DataGen_1345_increment_period.py
# = Purpose:     Update period tracker (YYYY-MM-DD); then merge base+delta into *_merged_new.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Period tracker: one row, one value YYYY-MM-DD. If empty use v_parm_dg_date_present;
# =    else add one DAY/WEEK/MONTH per v_parm_dg_period_type, save to file, set v_parm_dg_date_present_new.
# =  - Then: Random -> merge base+delta+merged to *_merged_new; Custom -> merge base+merged to *_merged_new.
# =  [END_1345]
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-07
# =  - Updated:
# ==================================================

import sys
import configparser
import logging
import os
from time import sleep
import json
import csv
import random
import pandas
import datetime
from datetime import datetime
import math

v_current_procedure_name = 'Increment period and merge (items, customers, matrix)'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

import pandas as pd
from datetime import datetime

v_date_format = '%Y-%m-%d'

# --- Period tracker: one row, one value YYYY-MM-DD ---
v_parm_dg_date_present_new = v_parm_dg_date_present
v_tracker_dir = os.path.dirname(v_parm_path_period_tracker)
if v_tracker_dir:
    os.makedirs(v_tracker_dir, exist_ok=True)

v_content = ""
if os.path.isfile(v_parm_path_period_tracker):
    with open(v_parm_path_period_tracker, 'r', encoding='utf-8') as f:
        v_content = f.read().strip()

if not v_content:
    v_parm_dg_date_present_new = v_parm_dg_date_present
    with open(v_parm_path_period_tracker, 'w', encoding='utf-8') as f:
        f.write(v_parm_dg_date_present_new + "\n")
    logging.debug("Period tracker empty; wrote v_parm_dg_date_present: " + v_parm_dg_date_present_new)
else:
    v_current_date_str = v_content.split()[0] if v_content else v_parm_dg_date_present
    v_current_dt = datetime.strptime(v_current_date_str, v_date_format)
    if v_parm_dg_period_type == "MONTH":
        v_freq = "MS"
    elif v_parm_dg_period_type == "WEEK":
        v_freq = "W-" + v_parm_dg_period_start_dow[0:3]
    else:
        v_freq = "D"
    v_temp_start = v_current_dt.strftime('%m-%d-%Y')
    v_list_next = pd.date_range(start=v_temp_start, periods=2, freq=v_freq)
    v_parm_dg_date_present_new = v_list_next[1].strftime(v_date_format)
    with open(v_parm_path_period_tracker, 'w', encoding='utf-8') as f:
        f.write(v_parm_dg_date_present_new + "\n")
    logging.debug("Period tracker incremented: " + v_current_date_str + " -> " + v_parm_dg_date_present_new)

# --- Merge: Random = base + delta + merged -> *_merged_new; Custom = base + merged -> *_merged_new ---
def read_csv_rows(path, skip_header=True):
    rows = []
    if not os.path.isfile(path):
        return rows
    with open(path, 'r', newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        for i, row in enumerate(r):
            if skip_header and i == 0:
                continue
            rows.append(tuple(row))
    return rows

def write_merged(path_out, header_row, data_rows):
    out_dir = os.path.dirname(path_out)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    seen = set()
    unique = []
    for row in data_rows:
        if row not in seen:
            seen.add(row)
            unique.append(row)
    unique.sort()
    with open(path_out, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header_row)
        for row in unique:
            w.writerow(row)
    logging.debug("Wrote " + str(len(unique)) + " rows to " + path_out)

def get_header(path):
    if not os.path.isfile(path):
        return None
    with open(path, 'r', newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        return next(r, None)

v_src = (v_parm_app_source_type or "").strip() if hasattr(v_parm_app_source_type, "strip") else str(v_parm_app_source_type or "")
if v_src != "Custom":
    v_src = "Random"

if v_src == "Random":
    # [a] items: base + delta + merged -> items_merged_new
    h = get_header(v_parm_path_items_base) or get_header(v_parm_path_items_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_items_base) + read_csv_rows(v_parm_path_items_delta) + read_csv_rows(v_parm_path_items_merged)
        write_merged(v_parm_path_items_merged_new, h, data)
    # [b] customers
    h = get_header(v_parm_path_customers_base) or get_header(v_parm_path_customers_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_customers_base) + read_csv_rows(v_parm_path_customers_delta) + read_csv_rows(v_parm_path_customers_merged)
        write_merged(v_parm_path_customers_merged_new, h, data)
    # [c] matrix
    h = get_header(v_parm_path_matrix_base) or get_header(v_parm_path_matrix_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_matrix_base) + read_csv_rows(v_parm_path_matrix_delta) + read_csv_rows(v_parm_path_matrix_merged)
        write_merged(v_parm_path_matrix_merged_new, h, data)
else:
    # [a] items: base + merged -> items_merged_new
    h = get_header(v_parm_path_items_base) or get_header(v_parm_path_items_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_items_base) + read_csv_rows(v_parm_path_items_merged)
        write_merged(v_parm_path_items_merged_new, h, data)
    # [b] customers
    h = get_header(v_parm_path_customers_base) or get_header(v_parm_path_customers_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_customers_base) + read_csv_rows(v_parm_path_customers_merged)
        write_merged(v_parm_path_customers_merged_new, h, data)
    # [c] matrix
    h = get_header(v_parm_path_matrix_base) or get_header(v_parm_path_matrix_merged)
    if h is not None:
        data = read_csv_rows(v_parm_path_matrix_base) + read_csv_rows(v_parm_path_matrix_merged)
        write_merged(v_parm_path_matrix_merged_new, h, data)

# [END_1345]

logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
