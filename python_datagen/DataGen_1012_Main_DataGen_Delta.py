# ==================================================
# = File:        DataGen_1012_Main_DataGen_Delta.py
# = Purpose:     Run delta DataGen pipeline: all 13xx scripts in sequence.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Calls: 1310, 1320, 1330, 1340, 1345, 1350, 1355, 1360, 1390.
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-07
# =  - Updated:
# ==================================================

import logging
import os
import shutil
import sys
from time import sleep

v_current_procedure_name = 'DataGenPY Delta'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

v_script_dir = os.path.dirname(os.path.abspath(__file__))
v_appDir = os.path.dirname(v_script_dir)
v_cwd = os.getcwd()
logging.debug("... initial working directory: [" + v_cwd + "]")
os.chdir(v_appDir)
logging.debug("... application working directory: [" + os.getcwd() + "]")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

# --- Mandatory base files: exit if any missing ---
v_base_paths = [
    ("items", v_parm_path_items_base),
    ("customers", v_parm_path_customers_base),
    ("organizations", v_parm_path_organizations_base),
    ("matrix", v_parm_path_matrix_base),
]
v_missing = [name for name, path in v_base_paths if not os.path.isfile(path)]
if v_missing:
    v_path_by_name = {name: path for name, path in v_base_paths}
    logging.error("Delta data generation requires all base files to exist. The following base file(s) do not exist:")
    for name in v_missing:
        logging.error("  - " + name + ": " + str(v_path_by_name[name]))
    logging.error("Existence of these base files is mandatory for any delta data generation.")
    sys.exit(1)

# --- Create merged files from base when missing ---
v_merged_specs = [
    (v_parm_path_items_merged, v_parm_path_items_base),
    (v_parm_path_customers_merged, v_parm_path_customers_base),
    (v_parm_path_organizations_merged, v_parm_path_organizations_base),
    (v_parm_path_matrix_merged, v_parm_path_matrix_base),
]
for v_merged_path, v_base_path in v_merged_specs:
    if not os.path.isfile(v_merged_path):
        v_merged_dir = os.path.dirname(v_merged_path)
        if v_merged_dir:
            os.makedirs(v_merged_dir, exist_ok=True)
        shutil.copy2(v_base_path, v_merged_path)
        logging.debug("Created merged file (copy of base): " + str(v_merged_path))

# --- 13xx delta sequence ---
if 1 == 1:
    from DataGen_1310_Generate_organizations_delta import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1320_Generate_items_delta import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1330_Generate_customers_delta import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1340_Generate_matrix_delta import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1345_increment_period import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1350_Generate_coredata_delta import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1355_prep_coredata import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1360_PostProcess_coredata import *
    logging.debug("\n" * 2)
    sleep(1)

if 1 == 1:
    from DataGen_1390_Compose_FBDI_Booking_History import *
    logging.debug("\n" * 2)
    sleep(1)

# ---
v_current_procedure_name = 'DataGenPY Delta'
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
