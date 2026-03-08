# ==================================================
# = File:        DataGen_1014_Main_Approve_and_consolidate_delta.py
# = Purpose:     Ask user to approve consolidation; backup merged files, then replace merged with merged_new.
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - If user answers Y/Yes (case insensitive): backup _merged and _merged_new to PATH_MERGED_BACKUP
# =    with timestamp prefix, then delete _merged, then rename _merged_new to _merged.
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-08
# =  - Updated:
# ==================================================

import logging
import os
import shutil
import sys
from datetime import datetime
from time import sleep

v_current_procedure_name = 'DataGenPY Approve and consolidate delta'

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

# --- Simple query: approve consolidation? ---
v_prompt = "Approve consolidation of new delta records?"
v_answer = input(v_prompt + " ").strip()
if v_answer.lower() not in ("y", "yes"):
    logging.debug("Consolidation not approved. Exiting.")
    logging.debug("==================================================")
    logging.debug("= " + v_current_procedure_name + ": END")
    logging.debug("==================================================")
    logging.debug("\n" * 2)
    sys.exit(0)

v_approval_success_status = True
v_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
v_backup_dir = v_parm_path_merged_backup
if v_backup_dir:
    os.makedirs(v_backup_dir, exist_ok=True)

def copy_to_backup(src_path, backup_dir, timestamp):
    """Copy file to backup_dir with timestamp prefix. Returns True on success, False on failure."""
    if not src_path or not os.path.isfile(src_path):
        return False
    basename = os.path.basename(src_path)
    dest_path = os.path.join(backup_dir, timestamp + "_" + basename)
    try:
        shutil.copy2(src_path, dest_path)
        return True
    except Exception:
        return False

# --- Backup: copy each _merged and _merged_new into backup with timestamp prefix ---
v_backup_specs = [
    v_parm_path_items_merged,
    v_parm_path_items_merged_new,
    v_parm_path_customers_merged,
    v_parm_path_customers_merged_new,
    v_parm_path_organizations_merged,
    v_parm_path_organizations_merged_new,
    v_parm_path_matrix_merged,
    v_parm_path_matrix_merged_new,
]
for v_src in v_backup_specs:
    if not copy_to_backup(v_src, v_backup_dir, v_timestamp):
        v_approval_success_status = False

if not v_approval_success_status:
    logging.error("There was an error backing up the NEW content; the approval process will stop and the OLD and NEW data will be left in place. Review and fix before attempting a new approval action.")
    logging.debug("==================================================")
    logging.debug("= " + v_current_procedure_name + ": END")
    logging.debug("==================================================")
    logging.debug("\n" * 2)
    sys.exit(1)

# --- Delete OLD merged files ---
v_old_merged_paths = [
    v_parm_path_items_merged,
    v_parm_path_customers_merged,
    v_parm_path_organizations_merged,
    v_parm_path_matrix_merged,
]
for v_path in v_old_merged_paths:
    if v_path and os.path.isfile(v_path):
        try:
            os.remove(v_path)
        except Exception:
            v_approval_success_status = False

if not v_approval_success_status:
    logging.error("There was an error deleting the OLD content in the MERGED directory; the approval process will stop and the OLD and NEW data will be left in place. Review and fix before attempting a new approval action.")
    logging.debug("==================================================")
    logging.debug("= " + v_current_procedure_name + ": END")
    logging.debug("==================================================")
    logging.debug("\n" * 2)
    sys.exit(1)

# --- Rename _merged_new to _merged ---
v_rename_specs = [
    (v_parm_path_items_merged_new, v_parm_path_items_merged),
    (v_parm_path_customers_merged_new, v_parm_path_customers_merged),
    (v_parm_path_organizations_merged_new, v_parm_path_organizations_merged),
    (v_parm_path_matrix_merged_new, v_parm_path_matrix_merged),
]
for v_src, v_dest in v_rename_specs:
    if v_src and os.path.isfile(v_src) and v_dest:
        try:
            os.rename(v_src, v_dest)
        except Exception:
            v_approval_success_status = False

if not v_approval_success_status:
    logging.error("There was an error renaming NEW to MERGED; review state and fix before attempting a new approval action.")
    logging.debug("==================================================")
    logging.debug("= " + v_current_procedure_name + ": END")
    logging.debug("==================================================")
    logging.debug("\n" * 2)
    sys.exit(1)

# --- Exit message ---
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
