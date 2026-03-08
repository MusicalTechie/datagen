# ==================================================
# = File:        DataGen_1290_Compose_FBDI_Booking_History.py
# = Purpose:     Select data from COREDATA (base) to compose an FBDI-formatted CSV file
# =              for loading into Oracle Fusion SCM.
# =
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  -
# =  -
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-FEB-24     Allan Barnard
# =  - Updated:     2026-FEB-24     Performance optimization (no logic changes)
# =  - Updated:
# =  - Updated:
# =
# ==================================================

import logging
import os
import csv
from datetime import datetime

v_current_procedure_name = 'Compose FBDI: Booking History'

from DataGen_1110_Load_config_main import *

v_log_enabled = int(v_parm_flag_loglevel) > 0

if v_log_enabled:
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
else:
    logging.basicConfig(level=logging.WARNING, format="%(message)s")

logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

v_path_coredata = v_parm_path_coredata_base
v_rowCounter_input = 0

with open(v_path_coredata, mode='r', newline='', encoding='utf-8') as v_fileHandle_input:

    v_csv_file_input_reader = csv.reader(v_fileHandle_input)

    v_fbdi_output_dir = os.path.dirname(v_parm_path_fbdi_booking)
    if v_fbdi_output_dir:
        os.makedirs(v_fbdi_output_dir, exist_ok=True)

    with open(v_parm_path_fbdi_booking, mode='w', newline='', encoding='utf-8', buffering=1024 * 1024) as v_filename_output:

        v_csv_file_output_writer = csv.writer(v_filename_output, quoting=csv.QUOTE_ALL)

        next(v_csv_file_input_reader)

        v_fbdi_header = [
            "Technical Name",
            "SR_INSTANCE_CODE",
            "PLAN_NAME",
            "MEASURE_NAME",
            "PRD_LVL_NAME",
            "PRD_LVL_MEMBER_NAME",
            "ORG_LVL_NAME",
            "ORG_LVL_MEMBER_NAME",
            "CUS_LVL_NAME",
            "CUS_LVL_MEMBER_NAME ",
            "CUS_SITE_LVL_MEMBER_NAME",
            "DCS_LVL_NAME",
            "DCS_LVL_MEMBER_NAME",
            "TIM_LVL_NAME",
            "TIM_LVL_MEMBER_VALUE",
            "VALUE_NUMBER",
            "ORDER_TYPE_FLAG",
            "DELETED_FLAG ",
            "SOR_LVL_NAME",
            "SOR_LVL_MEMBER_NAME"
        ]

        v_csv_file_output_writer.writerow(v_fbdi_header)

        v_fixed_f00 = ""
        v_fixed_f01 = "OPS"
        v_fixed_f02 = ""
        v_fixed_f03 = "Bookings History: Booked Item by Booked Date"
        v_fixed_f04 = "Item"
        v_fixed_f06 = "Organization"
        v_fixed_f07 = "002"
        v_fixed_f08 = "Customer Site"
        v_fixed_f11 = "Demand Class"
        v_fixed_f12 = "DC1"
        v_fixed_f13 = "Day"
        v_fixed_f16 = ""
        v_fixed_f17 = ""
        v_fixed_f18 = ""
        v_fixed_f19 = ""

        for v_row_input in v_csv_file_input_reader:

            v_rowCounter_input += 1

            if v_row_input[2] == "Accelworks Pvt Ltd":
                v_variable_f09 = "923497"
                v_variable_f10 = "1359648"
            elif v_row_input[2] == "Business World":
                v_variable_f09 = "16080"
                v_variable_f10 = "1091"
            elif v_row_input[2] == "Computer Service and Rental":
                v_variable_f09 = "10060-A"
                v_variable_f10 = "1310641"
            else:
                v_variable_f09 = "99999999"
                v_variable_f10 = "99999999"

            v_current_output_row = [
                v_fixed_f01,
                v_fixed_f02,
                v_fixed_f03,
                v_fixed_f04,
                v_row_input[1],
                v_fixed_f06,
                v_fixed_f07,
                v_fixed_f08,
                v_variable_f09,
                v_variable_f10,
                v_fixed_f11,
                v_fixed_f12,
                v_fixed_f13,
                datetime.strptime(v_row_input[0], "%Y-%m-%d").strftime("%Y/%m/%d"),
                v_row_input[3],
                v_fixed_f16,
                v_fixed_f17,
                v_fixed_f18,
                v_fixed_f19
            ]

            # --- CHANGED LINE: write unquoted, comma-separated data row ---
            v_filename_output.write(
                ','.join(str(v) if v is not None else '' for v in v_current_output_row) + '\n'
            )

logging.debug("Total FBDI BOOKING HISTORY data rows written : " + str(v_rowCounter_input))
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
