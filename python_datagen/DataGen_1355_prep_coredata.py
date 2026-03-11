# ==================================================
# = File:        DataGen_1355_prep_coredata.py
# = Purpose:     Combine coredata_merged + coredata_delta -> coredata_merged_new.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  [END_1355]
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

v_current_procedure_name = 'Prep coredata: merge + delta -> merged_new'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

# Create or overwrite coredata_merged_new = coredata_merged + coredata_delta
v_out_dir = os.path.dirname(v_parm_path_coredata_merged_new)
if v_out_dir:
    os.makedirs(v_out_dir, exist_ok=True)

v_header = None
v_rows = []
for v_path in [v_parm_path_coredata_merged, v_parm_path_coredata_delta]:
    if not os.path.isfile(v_path):
        continue
    with open(v_path, 'r', newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        for i, row in enumerate(r):
            if i == 0:
                if v_header is None:
                    v_header = row
                continue
            v_rows.append(row)

with open(v_parm_path_coredata_merged_new, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    if v_header:
        w.writerow(v_header)
    for row in v_rows:
        w.writerow(row)

logging.debug("Wrote " + str(len(v_rows)) + " data rows to " + v_parm_path_coredata_merged_new)
# [END_1355]

logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
