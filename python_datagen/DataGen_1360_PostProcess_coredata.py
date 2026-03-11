# ==================================================
# = File:        DataGen_1360_PostProcess_coredata.py
# = Purpose:     Post-process coredata_merged_new -> coredata2_merged_new (same logic as 1260).
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Sets env so 1260 uses merged_new paths when run.
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

v_current_procedure_name = 'PostProcess coredata_merged_new -> coredata2_merged_new'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

os.environ['DATAGEN_POSTPROCESS_MERGED_NEW'] = '1'

from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)

import DataGen_1260_PostProcess_coredata

logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
