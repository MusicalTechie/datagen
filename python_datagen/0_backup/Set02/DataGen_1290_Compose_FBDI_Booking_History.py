
# ==================================================
# = File:	    DataGen_1290_Compose_FBDI_Booking_History.py
# = Purpose:	Select data from COREDATA2 to compose an FBDI-formatted CSV file
# =             for loading into Oracle Fusion SCM.
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
# =  - Updated:     
# =  - Updated:
# =  - Updated:
# =
# ==================================================

# ---
# - Import Python libraries
# -
# - NOTE: you may have to install these within PyCharm
# -    - Open File > Settings > Project from the PyCharm menu.
# -     - Select your current project.
# -    - Click the Python Interpreter tab within your project tab.
# -    - Click the small + symbol to add a new library to the project.
# -    - Now type in the library to be installed, for example Pandas, and click Install Package
# ---
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

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Compose FBDI: Booking History'

# ---
# - Ensure logging goes to terminal (and to log file once 1110 is imported)
# ---
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# ---
# - Display a simple greeting
# ---
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n"*2)

# ---
# - Pick up primary application parameters
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
from DataGen_1110_Load_config_main import *
logging.debug("\n" * 2)
sleep(1)


# ---
# - Just a holding zone for pending code that will:
# -
# - 1) read the existing coredata2 file
# - 2) roll through the records while retaining various periods of data an calculate rolling or similar data
# - 3) write out the results (implies that it has to read several records before it can begin to write and
#      then writes the final records in the queue)
# -
# ---
if 1 == 1:

    # Set variables
    # Use a preceding "r" to create a "raw" string without any accidental escaped characters like "backslash-b"
    #v_path_customers = r"C:\GitHub_Local_Repository\AIML\AppsAssoc_DEV_DataGen_002_Python-Faker\data_results\base\Master_CUSTOMERS.csv"
    # -
    v_path_coredata          = v_parm_path_coredata_base
    v_path_coredata2         = v_parm_path_coredata2_base
    v_fileHandle_coredata    = ""
    v_fileHandle_coredata2   = ""
    v_rowCounter_input   = 0

    # ---
    # Reminder of relevant parameters
    # ---
    # v_parm_flag_loglevel = 0
    # ---
    if int(v_parm_flag_loglevel) > 0:
        logging.debug("-----")
        logging.debug("- Show the current date-related settings")
        logging.debug("-----")


    # ---
    # Output file variables
    # ---
    # v_parm_path_fbdi_booking
    # v_parm_path_fbdi_shipment

    # ---
    # - Open the source CSV file in "read-only" mode where the path name is in the variable v_parm_path_coredata2_base.  The column names are:
    # -     "Period","Item","Location","Orders_Complete","Orders_Open","Orders_Cancelled","Orders_Returned","Forecast01","Forecast02","Inventory_starting","Inventory_capacity","Inventory_production","Inventory_end","SafetyStock01","SafetyStock02","SafetyStock03","Net_Requirement","Outcome01","Outcome02","Outcome03","Trend_type","Trend_factor1","Trend_factor2","Trend_factor3","Trend_factor4","Trend_factor5","Last_Period","Last_X_Value","Last_Y_Value"
    # -
    # - Open the output CSV file in "write" mode where the path name is in the variable v_parm_path_fbdi_booking.  The column names are:
    # -     "DCS_LVL_NAME", "DCS_LVL_MEMBER_NAME", "TIM_LVL_NAME", "TIM_LVL_MEMBER_VALUE", "VALUE_NUMBER", "ORDER_TYPE_FLAG", "DELETED_FLAG ", "SOR_LVL_NAME", "SOR_LVL_MEMBER_NAME"
    # -
    # ---

    # Open the source file
    with open(v_parm_path_coredata2_base, mode='r', newline='') as v_fileHandle_input:

        if int(v_parm_flag_loglevel) > 0:
            logging.debug(" ")
            logging.debug("Opening INPUT file,  COREDATA ...")
            sleep(1)


        # Create the csv read-object
        v_csv_file_input_reader = csv.reader(v_fileHandle_input)


        # ---
        # - Open the output file
        # ---
        with open(v_parm_path_fbdi_booking, mode='w', newline='') as v_filename_output:

            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" ")
                logging.debug("Opening OUTPUT file, BOOKING HISTORY...")
                sleep(1)

            # Open the coredata2 "write object" for each loop
            v_csv_file_output_writer = csv.writer(v_filename_output, quoting=csv.QUOTE_ALL)


            # ---
            # - Walk through INPUT records.
            # ---
            # NOTE: these particular rows are "value only" and will read as "LIST" objects rather than "DICTIONARY" objects
            for v_row_input in v_csv_file_input_reader:

                # Update the row counter
                v_rowCounter_input += 1
                v_tempstr = str(v_rowCounter_input)

                # Temporary block to aid diagnostics
                if 1 == 2:
                    logging.debug('-----')
                    logging.debug(v_tempstr.rjust(3,'0') + ", " + str(type(v_row_input2)) + ", " + str(v_row_input2) + " ")
                    sleep(1)

                # ---
                # - If this is the first row, simply output it
                # ---
                if v_rowCounter_input == 1:

                    if int(v_parm_flag_loglevel) > 0:
                        logging.debug(" ")
                        logging.debug("Processing header row...")
                        sleep(1)

                    # Write out the target row
                    v_csv_file_output_writer.writerow("DCS_LVL_NAME", "DCS_LVL_MEMBER_NAME", "TIM_LVL_NAME", "TIM_LVL_MEMBER_VALUE", "VALUE_NUMBER", "ORDER_TYPE_FLAG", "DELETED_FLAG ", "SOR_LVL_NAME", "SOR_LVL_MEMBER_NAME")


                # ---
                # - If we're past the header, process every record.
                # ---
                if v_rowCounter_input > 1:

                    # Print a "remaining rows" indicator... but only for the 2nd record (no point repeating it)
                    if int(v_parm_flag_loglevel) > 0:
                        if v_rowCounter_input == 2:
                            logging.debug(" ")
                            logging.debug("Processing remaining rows...")
                            sleep(1)

                    if 1 == 1:
                        if int(v_parm_flag_loglevel) > 0:
                            logging.debug('Working on row: [' + str(v_rowCounter_input) + ']')
                            logging.debug(' - <' + str(v_row_input) + '>')
                            logging.debug(' ')
                            sleep(1)

                    # ---
                    # - Because these files could be quite large, occasionally print out an indication that stuff is happening.
                    # ---
                    if (v_rowCounter_input % 10000 == 0):
                        logging.debug('Working on row: [' + str(v_rowCounter_input) + ']')

                    # Input fields
                    # -        1       2         3            4               5                6               7                  8          9               10                  11                    12                   13              14                15                16             17              18       19            20          21           22               23            24              25               26             27             28              29
                    # -     "Period","Item","Location","Orders_Complete","Orders_Open","Orders_Cancelled","Orders_Returned","Forecast01","Forecast02","Inventory_starting","Inventory_capacity","Inventory_production","Inventory_end","SafetyStock01","SafetyStock02","SafetyStock03","Net_Requirement","Outcome01","Outcome02","Outcome03","Trend_type","Trend_factor1","Trend_factor2","Trend_factor3","Trend_factor4","Trend_factor5","Last_Period","Last_X_Value","Last_Y_Value"

                    # ---
                    # - Prepare field values into individual strings
                    # -
                    # - WARNING: field index values are in option base "0" so the first field is "0" and the 5th field is "4"
                    # ---

                    # - fixed value of "Demand Class"
                    v_f01_name = "DCS_LVL_NAME"
                    v_f01_value = "Demand Class"

                    # - fixed value of NULL
                    v_f02_name = "DCS_LVL_MEMBER_NAME"
                    v_f02_value = ""

                    # - fixed value of "Day"
                    v_f03_name = "TIM_LVL_NAME"
                    v_f03_value = "Day"

                    # - The time period (date), field #1 from the source file
                    v_f04_name = "TIM_LVL_MEMBER_VALUE"
                    v_f04_value = v_row_input[0]

                    # - The quantity.  Will presume field #4 from the source (orders).
                    v_f05_name = "VALUE_NUMBER"
                    v_f05_value = v_row_input[3]

                    # - fixed value of "External"
                    v_f06_name = "ORDER_TYPE_FLAG"
                    v_f06_value = "External"

                    # - fixed value of "NO"
                    v_f07_name = "DELETED_FLAG"
                    v_f07_value = "NO"

                    # - fixed value of "Sales Rep"
                    v_f08_name = "SOR_LVL_NAME"
                    v_f08_value = "Sales Rep"

                    # - fixed value of NULL
                    v_f09_name = "SOR_LVL_MEMBER_NAME"
                    v_f09_value = ""


                    # -
                    # - Prepare the record for writing.
                    # - Use the value "safety_stock_replace_me" as a target for eventual replacement with an
                    #   eventually-calculated rolling-average.
                    # -
                    v_current_output_row = '{ ' + '"' + v_f01_name + '"' + ": " + '"' + v_f01_value + '"' \
                                           + ', "' + v_f02_name + '"' + ": " + '"' + v_f02_value + '"' \
                                           + ', "' + v_f03_name + '"' + ": " + '"' + v_f03_value + '"' \
                                           + ', "' + v_f04_name + '"' + ": " + '"' + v_f04_value + '"' \
                                           + ', "' + v_f05_name + '"' + ": " + '"' + v_f05_value + '"' \
                                           + ', "' + v_f06_name + '"' + ": " + '"' + v_f06_value + '"' \
                                           + ', "' + v_f07_name + '"' + ": " + '"' + v_f07_value + '"' \
                                           + ', "' + v_f08_name + '"' + ": " + '"' + v_f08_value + '"' \
                                           + ', "' + v_f09_name + '"' + ": " + '"' + v_f09_value + '"' \
                                           + ' }'

                    # Convert the string to a JSON value
                    v_current_output_row_json = json.loads(v_current_output_row)

                    # Write out the result in CSV format
                    v_csv_file_output_writer.writerow(v_current_output_row_json.values())


# ---
# - Close the file
# ---
# NOTE: auto-closed when using "with open..."


# ---
# - Show total number of MATRIX rows created
# ---
logging.debug("\n"*2)
logging.debug("Total new FBDI BOOKING HISTORY rows created    : " + str(v_rowCounter_input) )
logging.debug("\n"*2)

# ---
# - Display exit message
# ---
v_current_procedure_name = 'Post-Process coredata2: Rolling calculations'
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n"*2)
sleep(1)
