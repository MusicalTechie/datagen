# ==================================================
# = File:        DataGen_1340_Generate_matrix_delta.py
# = Purpose:     Create MATRIX delta: associations between new ITEMs (from items_delta)
# =              and customers (base+delta if Random, base_custom if Custom). Output to matrix_delta.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Items source: v_parm_path_items_delta only.
# =  - Customers: (base + delta) if Random; (base_cstm only) if Custom.
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

v_current_procedure_name = 'Generate MATRIX: DELTA'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

v_parm_src = (v_parm_app_source_type or "").strip() if hasattr(v_parm_app_source_type, "strip") else str(v_parm_app_source_type or "")
if v_parm_src != "Custom":
    v_parm_src = "Random"
if v_parm_src == "Custom":
    v_path_customers_list = [v_parm_path_customers_base_cstm]
    logging.debug("Source type: Custom -> CUSTOMERS from " + str(v_parm_path_customers_base_cstm))
else:
    v_path_customers_list = [v_parm_path_customers_base, v_parm_path_customers_delta]
    logging.debug("Source type: Random -> CUSTOMERS from base + delta")

v_path_items = v_parm_path_items_delta
v_path_matrix = v_parm_path_matrix_delta
v_output_dir = os.path.dirname(v_path_matrix)
if v_output_dir:
    os.makedirs(v_output_dir, exist_ok=True)

# Load existing (Item, Location) keys from matrix_merged and matrix_delta (key = first two columns)
v_matrix_key_col_item, v_matrix_key_col_location = 0, 1
v_existing_matrix_keys = set()
for v_m_path in [v_parm_path_matrix_merged, v_parm_path_matrix_delta]:
    if not os.path.isfile(v_m_path):
        continue
    with open(v_m_path, mode='r', newline='', encoding='utf-8') as v_f:
        v_m_reader = csv.reader(v_f)
        for v_m_i, v_m_row in enumerate(v_m_reader):
            if v_m_i == 0:
                continue
            if len(v_m_row) >= 2:
                v_existing_matrix_keys.add((v_m_row[v_matrix_key_col_item].strip(), v_m_row[v_matrix_key_col_location].strip()))

# Collect all customer rows (skip headers) from the chosen files
v_list_customer_rows = []
for v_path_c in v_path_customers_list:
    if not os.path.isfile(v_path_c):
        continue
    with open(v_path_c, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            v_list_customer_rows.append(row)

v_rowCounter_matrix = 0
with open(v_path_matrix, mode='w', newline='', encoding='utf-8') as v_fileHandle_matrix:
    v_csv_file_matrix_writer = csv.writer(v_fileHandle_matrix, quoting=csv.QUOTE_ALL)
    v_current_output_row_json_list = json.loads(v_parm_dg_matrix_col_names)
    v_current_output_row_json_dict = v_current_output_row_json_list[0] if v_current_output_row_json_list else {}
    v_csv_file_matrix_writer.writerow(v_current_output_row_json_dict.values())

    with open(v_path_items, mode='r', newline='', encoding='utf-8') as v_fileHandle_items:
        v_csv_file_item_reader = csv.reader(v_fileHandle_items)
        for v_row_index, v_row_item in enumerate(v_csv_file_item_reader):
            if v_row_index == 0:
                continue
            for v_row_customer in v_list_customer_rows:
                if random.randint(1, 100) > int(v_parm_dg_attach_rate):
                    continue
                v_f01_value = v_row_item[-1].strip() if v_row_item else ""
                v_f02_value = v_row_customer[-1].strip() if v_row_customer else ""
                v_matrix_key = (v_f01_value, v_f02_value)
                if v_matrix_key in v_existing_matrix_keys:
                    continue
                v_existing_matrix_keys.add(v_matrix_key)
                v_rowCounter_matrix += 1
                v_f01_name, v_f02_name = "Item", "Location"
                v_temp_rnd = random.randint(1, 100)
                v_f03_value = "Inactive" if v_temp_rnd <= 25 else "Active"
                v_temp_rnd = random.randint(1, 100)
                if v_temp_rnd <= 25:
                    v_f04_value = "NPI"
                elif v_temp_rnd <= 50:
                    v_f04_value = "Core"
                else:
                    v_f04_value = "EOL"
                v_trends = ["Intermittent01", "Slope01", "Seasonal01", "Combined01"]
                v_f05_value = v_trends[min(3, random.randint(1, 100) // 34)]
                v_f06_value = v_trends[min(3, random.randint(1, 100) // 34)]
                v_f07_value = v_trends[min(3, random.randint(1, 100) // 34)]
                v_f08_value, v_f09_value, v_f10_value = "2023-01-01", "2023-01-01", "2027-01-01"
                v_f11_value = "Rolling_6-Period_Average"
                v_f12_value = str(random.randint(1, 100))
                v_current_output_row = '{ "' + v_f01_name + '": "' + v_f01_value + '"' \
                    + ', "' + v_f02_name + '": "' + v_f02_value + '"' \
                    + ', "Status": "' + v_f03_value + '"' \
                    + ', "LifeCycle": "' + v_f04_value + '"' \
                    + ', "TrendNPI": "' + v_f05_value + '"' \
                    + ', "TrendCORE": "' + v_f06_value + '"' \
                    + ', "TrendEOL": "' + v_f07_value + '"' \
                    + ', "DateNPI": "' + v_f08_value + '"' \
                    + ', "DateCORE": "' + v_f09_value + '"' \
                    + ', "DateEOL": "' + v_f10_value + '"' \
                    + ', "SafetyStockType": "' + v_f11_value + '"' \
                    + ', "InitialSafetyStockValue": "' + v_f12_value + '" }'
                v_current_output_row_json = json.loads(v_current_output_row)
                v_csv_file_matrix_writer.writerow(v_current_output_row_json.values())

logging.debug("\n" * 2)
logging.debug("ITEM-to-LOCATION attach-rate : " + str(v_parm_dg_attach_rate) + "%")
logging.debug("Total new MATRIX delta rows created: " + str(v_rowCounter_matrix))
logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
