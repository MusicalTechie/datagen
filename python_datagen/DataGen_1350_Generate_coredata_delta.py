# ==================================================
# = File:        DataGen_1350_Generate_coredata_delta.py
# = Purpose:     Generate coredata from v_parm_dg_date_present_new to v_parm_dg_date_future_end
# =              into v_parm_path_coredata_delta (uses same logic as 1250 in delta mode).
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Period tracker (updated by 1345) holds the start date; 1250 reads it when DATAGEN_COREDATA_DELTA=1.
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-07
# =  - Updated:
# ==================================================

import os
import logging
from time import sleep

v_current_procedure_name = 'Generate COREDATA: DELTA'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

# Delta mode: 1250 will use period_tracker start date, matrix_merged_new, coredata_delta
os.environ['DATAGEN_COREDATA_DELTA'] = '1'

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

# Run the same generation as 1250 but with delta date range and paths (handled inside 1250)
import DataGen_1250_Generate_coredata_initial

logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
