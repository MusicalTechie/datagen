
# ==================================================
# = File:	    DataGen_1250_PostProcess_coredata2.py
# = Purpose:	Post-process the coredata2 file to calculate values such as "rolling averages"
# =
# = WARNING:
# =             coredata2 is a TEMPORARY file.  It helps everyone to see more advanced
# =             data without having to connect to Oracle or Snowflake.
# =
# =             However... once we get constant and familiar connections to Oracle and
# =             Snowflake, these rolling-average or other statistical functions
# =             should be done by SQL or similar commands... much faster and smarter.
# =
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Options for calculation:
# =    - fake inventory functions
# =    - rolling-average to use as one method of calculating initial safety-stock
# =    - determining better/worse LABELS of various types (better/indeterminate/worse, -5 to +5, etc)
# =  -
# =  - 
# = 
# = Dates:
# = ------------------------------------------------
# =  - Created:     2022-FEB-24     Allan Barnard, no content yet... just a shell
# =  - Updated:     2022-MAR-04     Allan, Satish, Myles... add basic loops through coredata2 to produce coredata2
# =  - Updated:     2022-APR-06     Allan, load improved coredata2, perform rolling-average for Safety Stock, improve inventory calculations
# =  - Updated:     2022-APR-07     Allan, add FIFO queue for output rows, inventory consumption, etc.
# =  - Updated:
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
import os
import time
import json
import csv
import random
import pandas
import datetime
from datetime import datetime

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Post-Process coredata2: Rolling calculations'


# ---
# - Display a simple greeting
# ---
print("==================================================")
print("= " + v_current_procedure_name + ": START")
print("==================================================")
print("\n"*2)

# ---
# - Pick up primary application parameters
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
from DataGen_1110_Load_config_main import *
print("\n" * 2)
sleep(1)



# ---
# - Convert some variable content from JSON to LIST form
# -
# - TRENDS
# - DG_OUTCOME_RANGE
# - DG_OUTCOME_TRIGGER
# - DG_OUTCOME_FIX
# ---

# TEST LINE: optionally hard-code the loglevel flag to be high
v_parm_flag_loglevel=0

# TRENDS
if 1 == 1:
    # Get TRENDS
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_dmd_trends \n<\n" + v_parm_dg_dmd_trends + "\n>")
            print('---')
        v_list_dmd_trends = json.loads(v_parm_dg_dmd_trends)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_dmd_trends')
            print('List   : ' + 'v_list_dmd_trends')
            print('Type   : ' + str(type(v_list_dmd_trends)))
            print('Count  : ' + str(len(v_list_dmd_trends)))
            print('---')
        for v_parent_element in v_list_dmd_trends:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element))
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n" * 2)

# DG_OUTCOME_RANGE
if 1 == 1:
    # Get DG_OUTCOME_RANGE
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_outcome_range \n<\n" + v_parm_dg_outcome_range + "\n>")
            print('---')
        v_list_outcome_range = json.loads(v_parm_dg_outcome_range)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_outcome_range')
            print('List   : ' + 'v_list_outcome_range')
            print('Type   : ' + str(type(v_list_outcome_range)))
            print('Count  : ' + str(len(v_list_outcome_range)))
            print('---')
        for v_parent_element in v_list_outcome_range:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element))
            # for v_child_element in v_parent_element:
            #     if int(v_parm_flag_loglevel) > 0:
            #         print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n" * 2)

# DG_OUTCOME_TRIGGER
if 1 == 1:
    # Get DG_OUTCOME_TRIGGER
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_outcome_trigger \n<\n" + v_parm_dg_outcome_trigger + "\n>")
            print('---')
        v_list_outcome_trigger = json.loads(v_parm_dg_outcome_trigger)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_outcome_trigger')
            print('List   : ' + 'v_list_outcome_trigger')
            print('Type   : ' + str(type(v_list_outcome_trigger)))
            print('Count  : ' + str(len(v_list_outcome_trigger)))
            print('---')
        for v_parent_element in v_list_outcome_trigger:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element))
            # for v_child_element in v_parent_element:
            #     if int(v_parm_flag_loglevel) > 0:
            #         print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n" * 2)

# DG_OUTCOME_FIX
if 1 == 1:
    # Get DG_OUTCOME_FIX
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_outcome_fix \n<\n" + v_parm_dg_outcome_fix + "\n>")
            print('---')
        v_list_outcome_fix = json.loads(v_parm_dg_outcome_fix)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_outcome_fix')
            print('List   : ' + 'v_list_outcome_fix')
            print('Type   : ' + str(type(v_list_outcome_fix)))
            print('Count  : ' + str(len(v_list_outcome_fix)))
            print('---')
        for v_parent_element in v_list_outcome_fix:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element))
            # for v_child_element in v_parent_element:
            #     if int(v_parm_flag_loglevel) > 0:
            #         print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n" * 2)

# ---
# - Optional test line
# ---
if 1 == 2:
    print('-----')
    print('- Forced exit!')
    print('-----')
    print(' ')
    sleep(1)
    quit()



# ---
# - TEST LINE ONLY
# - If you want to force enable/disable screen-logging "on" temporarily, just comment this line in or out.
# ---
# v_parm_flag_loglevel = 0
# v_parm_flag_loglevel = 1


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
    v_rowCounter_coredata2   = 0

    # ---
    # Reminder of relevant parameters
    # ---
    # v_parm_flag_loglevel = 0
    # ---
    if int(v_parm_flag_loglevel) > 0:
        print("-----")
        print("- Show the current date-related settings")
        print("-----")
    # ---
    v_parm_current = "DG_CALENDAR_TYPE"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_calendar_type + "]")
    # ---
    v_parm_current = "DG_PERIOD_START"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_period_start + "]")
    # ---
    v_parm_current = "DG_PERIOD_START_DoW"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_period_start_dow + "]")
    # ---
    v_parm_current = "DG_PERIOD_DIRECTION"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_period_direction + "]")
    # ---
    v_parm_current = "DG_DATE_HISTORY_START"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_history_start + "]")
    # ---
    v_parm_current = "DG_DATE_HISTORY_END"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_history_end + "]")
    # ---
    v_parm_current = "DG_DATE_PRESENT"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_present + "]")
    # ---
    v_parm_current = "DG_DATE_OPENORDERS_START"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_openorders_start + "]")
    # ---
    v_parm_current = "DG_DATE_OPENORDERS_END"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_openorders_end + "]")
    # ---
    v_parm_current = "DG_DATE_FUTURE_START"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_future_start + "]")
    # ---
    v_parm_current = "DG_DATE_FUTURE_END"
    if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_date_future_end + "]")
    # ---

    # ---
    # - Convert parameters that are STRING values to DATE objects
    # ---
    # NOTE: sample date-time format elements include: '%d/%m/%y %H:%M:%S'
    v_date_format = '%Y-%m-%d'
    v_date_history_start = datetime.strptime(v_parm_dg_date_history_start, v_date_format)
    v_date_history_end = datetime.strptime(v_parm_dg_date_history_end, v_date_format)
    v_date_present = datetime.strptime(v_parm_dg_date_present, v_date_format)
    v_date_openorders_start = datetime.strptime(v_parm_dg_date_openorders_start, v_date_format)
    v_date_openorders_end = datetime.strptime(v_parm_dg_date_openorders_end, v_date_format)
    v_date_future_start = datetime.strptime(v_parm_dg_date_future_start, v_date_format)
    v_date_future_end = datetime.strptime(v_parm_dg_date_future_end, v_date_format)
    # print("")
    # print('Type of v_date_start: ' + str(type(v_date_start)) )

    # ---
    # - Get some DATE values
    # ---
    # NOTE: sample date-time format elements include: '%d/%m/%y %H:%M:%S'
    v_date_format = '%Y-%m-%d'
    v_date_present = datetime.strptime(v_parm_dg_date_present, v_date_format)
    #v_date_present_str = v_date_present.strftime('%m-%d-%Y')
    v_date_present_str = v_date_present.strftime(v_date_format)

    # ---
    # - Prepare variables to detect changes in the KEY
    # ---
    v_keyCounter            = 0
    v_keyValue_prior        = "n/a"
    v_keyValue_current      = ""
    v_keyValue_date_prior   = datetime.strptime('2000-01-01', v_date_format)
    v_keyValue_date_current = datetime.strptime('2001-01-01', v_date_format)

    # ---
    # - Prepare a variable to be either/both of HISTORY or FORECAST depending on the time period involved
    # -    - use the ORDERS_COMPLETED if this is a HISTORICAL PERIOD
    # -    - use the FORECAST01 if this is a PRESENT or FUTURE PERIOD
    # ---
    v_effective_order_volume = float("0.0")

    # ---
    # - Prepare some simple values for tracking a six-period rolling average
    # -
    # - NOTE: libraries like PANDAS and NUMPY can perform rolling averages with functions
    # - NOTE: this should be done with arrays (at the least) to allow a variable number of periods to be considered.
    # -       Cheating for now and setting it for 6 periods.
    # ---
    v_safety_stock_rolling_avg_num_of_periods = 6
    v_safety_stock_value_01 = 0
    v_safety_stock_value_02 = 0
    v_safety_stock_value_03 = 0
    v_safety_stock_value_04 = 0
    v_safety_stock_value_05 = 0
    v_safety_stock_value_06 = 0

    # ---
    # - Prepare variables to act as a FIFO queue for rows of data.
    # -
    # - Several rows have to be stored until a forward-looking rolling-average can be calculated.
    # - Then the eventually-calculated value needs to be inserted into the oldest row in the queue and written out
    # ---
    v_coredata2_row_01 = ""
    v_coredata2_row_02 = ""
    v_coredata2_row_03 = ""
    v_coredata2_row_04 = ""
    v_coredata2_row_05 = ""
    v_coredata2_row_06 = ""

    # ---
    # - Open COREDATA to READ the rows
    # ---
    with open(v_path_coredata, mode='r', newline='') as v_fileHandle_coredata:

        if int(v_parm_flag_loglevel) > 0:
            print(" ")
            print("Opening READ file,  COREDATA ...")
            sleep(1)

        # Create the csv read-object
        v_csv_file_coredata_reader = csv.reader(v_fileHandle_coredata)

        # ---
        # - Open the target file (COREDATA2) for eventual writing of a new record
        # ---
        with open(v_path_coredata2, mode='w', newline='') as v_fileHandle_coredata2:

            if int(v_parm_flag_loglevel) > 0:
                print(" ")
                print("Opening WRITE file, COREDATA2...")
                sleep(1)

            # Open the coredata2 "write object" for each loop
            v_csv_file_coredata2_writer = csv.writer(v_fileHandle_coredata2, quoting=csv.QUOTE_ALL)

            # ---
            # - Walk through COREDATA records.  Keep track of several periods so
            # - rolling calculations can be performed.  Write a record once a rolling
            # - limit is hit.
            # ---
            # NOTE: these particular rows are "value only" and will read as "LIST" objects rather than "DICTIONARY" objects
            for v_row_coredata in v_csv_file_coredata_reader:

                # Update the row counter
                v_rowCounter_coredata2 += 1
                v_tempstr = str(v_rowCounter_coredata2)

                # Temporary block to aid diagnostics
                if 1 == 2:
                    print('-----')
                    print(v_tempstr.rjust(3,'0') + ", ", end = "")
                    print(str(type(v_row_coredata2)) + ", ", end = "")
                    print(v_row_coredata2)
                    print(' ')
                    sleep(1)

                # ---
                # - If this is the first row, simply output it
                # ---
                if v_rowCounter_coredata2 == 1:

                    if int(v_parm_flag_loglevel) > 0:
                        print(" ")
                        print("Processing header row...")
                        sleep(1)

                    # Write out the target row
                    v_csv_file_coredata2_writer.writerow(v_row_coredata)


                # ---
                # - If we're past the header, process every record.
                # ---
                if v_rowCounter_coredata2 > 1:

                    # Print a "remaining rows" indicator... but only for the 2nd record (no point repeating it)
                    if int(v_parm_flag_loglevel) > 0:
                        if v_rowCounter_coredata2 == 2:
                            print(" ")
                            print("Processing remaining rows...")
                            sleep(1)

                    if 1 == 1:
                        if int(v_parm_flag_loglevel) > 0:
                            print('Working on row: [', str(v_rowCounter_coredata2), ']')
                            print(' - <' + str(v_row_coredata) + '>')
                            print(' ')
                            sleep(1)

                    # ---
                    # - Because these files could be quite large, occasionally print out an indication that stuff is happening.
                    # ---
                    if (v_rowCounter_coredata2 % 10000 == 0):
                        print('Working on row: [', str(v_rowCounter_coredata2), ']')

                    # ---
                    # - Prepare field values into individual strings
                    # ---
                    v_f01_name = "Period"
                    v_f01_value = v_row_coredata[0]

                    # -
                    v_f02_name = "Item"
                    v_f02_value = v_row_coredata[1]

                    # -
                    v_f03_name = "Location"
                    v_f03_value = v_row_coredata[2]

                    # -
                    v_f04_name = "Orders_Complete"
                    v_f04_value = v_row_coredata[3]

                    # -
                    v_f05_name = "Orders_Open"
                    v_f05_value = v_row_coredata[4]

                    # -
                    v_f06_name = "Orders_Cancelled"
                    v_f06_value = v_row_coredata[5]

                    # -
                    v_f07_name = "Orders_Returned"
                    v_f07_value = v_row_coredata[6]

                    # -
                    v_f08_name = "Orders_Forecast01"
                    v_f08_value = v_row_coredata[7]

                    # -
                    v_f09_name = "Orders_Forecast02"
                    v_f09_value = v_row_coredata[8]

                    # -
                    v_f10_name = "Inventory_starting"
                    v_f10_value = v_row_coredata[9]

                    # -
                    v_f11_name = "Inventory_capacity"
                    v_f11_value = v_row_coredata[10]

                    # -
                    v_f12_name = "Inventory_production"
                    v_f12_value = v_row_coredata[11]

                    # -
                    v_f13_name = "Inventory_end"
                    v_f13_value = v_row_coredata[12]

                    # -
                    v_f14_name = "SafetyStock01"
                    v_f14_value = v_row_coredata[13]

                    # -
                    v_f15_name = "SafetyStock02"
                    v_f15_value = v_row_coredata[14]

                    # -
                    v_f16_name = "SafetyStock03"
                    v_f16_value = v_row_coredata[15]

                    # ---
                    # - Check to see if the key (e.g. ITEM and LOC combined) has changed.
                    # -     - if so,  clear some variables
                    # -     - if not, then sum some values
                    # ---
                    v_keyValue_current = v_f02_value + ":" + v_f03_value
                    v_keyValue_date_current = datetime.strptime(v_f01_value, v_date_format)

                    # Check for the KEY (e.g. Item+Location) changing
                    #   - if so then print a line (optionally), increment the key counter, and clear out the "effective order volume"
                    if v_keyValue_current != v_keyValue_prior:
                        v_keyCounter += 1
                        v_effective_order_volume = 0
                        v_safety_stock_value_01 = 0
                        v_safety_stock_value_02 = 0
                        v_safety_stock_value_03 = 0
                        v_safety_stock_value_04 = 0
                        v_safety_stock_value_05 = 0
                        v_safety_stock_value_06 = 0
                        #v_csv_file_coredata2_writer.writerow("----------")

                    # Check to see if this is HISTORY or FUTURE and add ORDERS if in the past and FORECAST if in the FUTURE
                    # to the "effective order volume" that will be used to for the rolling average in turn used to
                    # calculate "safety stock"
                    #
                    # NOTE: This value will be left here in case it is useful in the future.
                    #       However, neither DEMAND or FORECAST will be used to affect the safety-stock as of 2022-May-17
                    #
                    if v_keyValue_date_current < v_date_present:
                        # This is HISTORY so use "orders complete" as the volume
                        v_effective_order_volume = float(v_f04_value)
                    else:
                        # Otherwise, this is FUTURE so use "forecast" as the volume
                        v_effective_order_volume = float(v_f08_value)

                    # ---
                    # - Perform a FIFO and a SUM of the existing and simple safety-stock value
                    # - in field #14.
                    # -
                    # - NOTE: variable 06 is the oldest and 01 is the newest.
                    # ---
                    v_safety_stock_value_06 = v_safety_stock_value_05
                    v_safety_stock_value_05 = v_safety_stock_value_04
                    v_safety_stock_value_04 = v_safety_stock_value_03
                    v_safety_stock_value_03 = v_safety_stock_value_02
                    v_safety_stock_value_02 = v_safety_stock_value_01
                    v_safety_stock_value_01 = int(float(v_f14_value))

                    # ---
                    # - Calculate the new rolling average value for Safety Stock
                    # ---
                    v_safety_stock_rolling_avg = (v_safety_stock_value_01 + v_safety_stock_value_02 + v_safety_stock_value_03 + v_safety_stock_value_04 + v_safety_stock_value_05 + v_safety_stock_value_06) / v_safety_stock_rolling_avg_num_of_periods

                    # ---
                    # - Multiply the rolling-average (smoothed safety stock) by some factor from config file
                    # ---
                    v_safety_stock_rolling_avg_mod = int(v_safety_stock_rolling_avg * float(v_parm_dg_dmd_ss_factor))

                    # -
                    v_f17_name = "Net_Requirement"
                    v_f17_value = v_row_coredata[16]


                    # - F18
                    # -
                    v_f18_name = "Outcome01"

                    # - Determine an initial label value
                    # - Then make an effort to convert that to a corrective value
                    # - Then set a new and hopefully improved safety stock value.
                    # - parameter values: v_parm_dg_outcome_range, v_parm_dg_outcome_trigger, v_parm_dg_outcome_fix
                    # - LIST VALUES     : v_list_outcome_range, v_list_outcome_trigger, v_list_outcome_fix
                    #
                    # Example:
                        # DG_OUTCOME_RANGE   = [{"Field01": "VeryLow", "Field02": "Low", "Field03": "OK", "Field04": "High","Field05": "VeryHigh"}]
                        # DG_OUTCOME_TRIGGER = [{"Field01": ".50", "Field02": ".75", "Field03": "1.00", "Field04": "1.25","Field05": "1.50"}]
                        # DG_OUTCOME_FIX	  = [{"Field01": "1.50", "Field02": "1.25", "Field03": "1.00", "Field04": ".75", "Field05": ".50"}]

                        # These are here simply for reference; will only use in the COREDATA2 program
                        # as it calculates ending-inventory which informs the LABEL
                        #
                        # For now, presume there are only five possible LABEL values.
                        # Later this section can be converted to scan the number of options and perform a variable IF-THEN.

                        # for v_parent_element in v_list_outcome_fix:
                        #     if int(v_parm_flag_loglevel) > 0:
                        #         print(" - Parent row: " + str(v_parent_element))
                        #     for v_child_element in v_parent_element:
                        #         if int(v_parm_flag_loglevel) > 0:
                        #             print("   - " + v_child_element + ": [" + v_parent_element[
                        #                 v_child_element] + "]")

                    v_ending_inventory = float(v_f13_value)
                    v_rolling_safety_stock = float(v_safety_stock_rolling_avg)
                    v_rolling_safety_stock_mod = float(v_safety_stock_rolling_avg_mod)

                    # Presume the evaluation of a LABEL starts with "OK", or index "2" of 0,1,2,3,4
                    v_index_value = int(2)
                    # print("v_index_value: ", v_index_value)
                    # print("v_list_outcome_range: ", v_list_outcome_range)
                    # print("v_list_outcome_range[v_index_value]: ", v_list_outcome_range[0])
                    # sleep(2)
                    v_outcome_text = v_list_outcome_range[v_index_value]
                    v_outcome_trigger = float(v_list_outcome_trigger[v_index_value])
                    v_outcome_fix = float(v_list_outcome_fix[v_index_value])

                    # VeryLow
                    v_index_value = 0
                    v_temp_comparison = float( v_list_outcome_trigger[v_index_value] )
                    if v_rolling_safety_stock < (v_ending_inventory * v_temp_comparison):
                        v_outcome_text = v_list_outcome_range[v_index_value]
                        v_outcome_trigger = float(v_list_outcome_trigger[v_index_value])
                        v_outcome_fix = float(v_list_outcome_fix[v_index_value])
                    else:
                        # Low
                        v_index_value = 1
                        v_temp_comparison = float( v_list_outcome_trigger[v_index_value] )
                        if v_rolling_safety_stock < (v_ending_inventory * v_temp_comparison):
                            v_outcome_text = v_list_outcome_range[v_index_value]
                            v_outcome_trigger = float(v_list_outcome_trigger[v_index_value])
                            v_outcome_fix = float(v_list_outcome_fix[v_index_value])
                        else:
                            # VeryHigh
                            v_index_value = 4
                            v_temp_comparison = float( v_list_outcome_trigger[v_index_value] )
                            if v_rolling_safety_stock > (v_ending_inventory * v_temp_comparison):
                                v_outcome_text = v_list_outcome_range[v_index_value]
                                v_outcome_trigger = float(v_list_outcome_trigger[v_index_value])
                                v_outcome_fix = float(v_list_outcome_fix[v_index_value])
                            else:
                                # High
                                v_index_value = 3
                                v_temp_comparison = float( v_list_outcome_trigger[v_index_value] )
                                if v_rolling_safety_stock > (v_ending_inventory * v_temp_comparison):
                                    v_outcome_text = v_list_outcome_range[v_index_value]
                                    v_outcome_trigger = float(v_list_outcome_trigger[v_index_value])
                                    v_outcome_fix = float(v_list_outcome_fix[v_index_value])

                    #v_f18_value = v_row_coredata[17]
                    v_f18_value = v_outcome_text + ", fix with: " + str(v_outcome_fix)

                    # - F19
                    # - Temporarily using this to show the corrected safety-stock value... should be fed to the AI/ML engine
                    v_f19_name = "Outcome02"
                    #v_f19_value = v_row_coredata[18]
                    v_f19_value = str(int(float(v_rolling_safety_stock) * v_outcome_fix))

                    # -
                    v_f20_name = "Outcome03"
                    v_f20_value = v_row_coredata[19]

                    # -
                    v_f21_name = "Trend_type"
                    v_f21_value = v_row_coredata[20]

                    # -
                    v_f22_name = "Trend_factor1"
                    v_f22_value = v_row_coredata[21]

                    # -
                    v_f23_name = "Trend_factor2"
                    v_f23_value = v_row_coredata[22]

                    # -
                    v_f24_name = "Trend_factor3"
                    v_f24_value = v_row_coredata[23]

                    # -
                    v_f25_name = "Trend_factor4"
                    v_f25_value = v_row_coredata[24]

                    # -
                    v_f26_name = "Trend_factor5"
                    v_f26_value = v_row_coredata[25]

                    # -
                    v_f27_name = "Last_Period"
                    v_temp_val = v_row_coredata[26]
                    v_f27_value = str(v_temp_val)

                    # -
                    v_f28_name = "Last_X_Value"
                    v_temp_val = v_row_coredata[27]
                    v_f28_value = str(v_temp_val)

                    # -
                    v_f29_name = "Last_Y_Value"
                    v_temp_val = v_row_coredata[28]
                    v_f29_value = str(v_temp_val)


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
                                           + ', "' + v_f10_name + '"' + ": " + '"' + v_f10_value + '"' \
                                           + ', "' + v_f11_name + '"' + ": " + '"' + v_f11_value + '"' \
                                           + ', "' + v_f12_name + '"' + ": " + '"' + v_f12_value + '"' \
                                           + ', "' + v_f13_name + '"' + ": " + '"' + v_f13_value + '"' \
                                           + ', "' + v_f14_name + '"' + ": " + '"' + v_f14_value + '"' \
                                           + ', "' + v_f15_name + '"' + ": " + '"' + "safety_stock_replace_me_01" + '"' \
                                           + ', "' + v_f16_name + '"' + ": " + '"' + "safety_stock_replace_me_02" + '"' \
                                           + ', "' + v_f17_name + '"' + ": " + '"' + v_f17_value + '"' \
                                           + ', "' + v_f18_name + '"' + ": " + '"' + v_f18_value + '"' \
                                           + ', "' + v_f19_name + '"' + ": " + '"' + v_f19_value + '"' \
                                           + ', "' + v_f20_name + '"' + ": " + '"' + "outcome03_replace_me" + '"' \
                                           + ', "' + v_f21_name + '"' + ": " + '"' + v_f21_value + '"' \
                                           + ', "' + v_f22_name + '"' + ": " + '"' + v_f22_value + '"' \
                                           + ', "' + v_f23_name + '"' + ": " + '"' + v_f23_value + '"' \
                                           + ', "' + v_f24_name + '"' + ": " + '"' + v_f24_value + '"' \
                                           + ', "' + v_f25_name + '"' + ": " + '"' + v_f25_value + '"' \
                                           + ', "' + v_f26_name + '"' + ": " + '"' + v_f26_value + '"' \
                                           + ', "' + v_f27_name + '"' + ": " + '"' + v_f27_value + '"' \
                                           + ', "' + v_f28_name + '"' + ": " + '"' + v_f28_value + '"' \
                                           + ', "' + v_f29_name + '"' + ": " + '"' + v_f29_value + '"' \
                                           + ' }'


                    # ---
                    # - Only write out the row from six periods ago at this time
                    # - (since we had to collect six to do rolling averages)
                    # -
                    # - Otherwise, store the values in a FIFO queue.
                    # -
                    # - Shift the FIFO queue below...
                    # ---
                    v_coredata2_row_06 = v_coredata2_row_05
                    v_coredata2_row_05 = v_coredata2_row_04
                    v_coredata2_row_04 = v_coredata2_row_03
                    v_coredata2_row_03 = v_coredata2_row_02
                    v_coredata2_row_02 = v_coredata2_row_01
                    v_coredata2_row_01 = v_current_output_row

                    if 1 == 2:
                        if int(v_parm_flag_loglevel) > 0:
                            print('- FIFO queue: ')
                            print('   06 <' + str(v_coredata2_row_06) + '>')
                            print('   05 <' + str(v_coredata2_row_05) + '>')
                            print('   04 <' + str(v_coredata2_row_04) + '>')
                            print('   03 <' + str(v_coredata2_row_03) + '>')
                            print('   02 <' + str(v_coredata2_row_02) + '>')
                            print('   01 <' + str(v_coredata2_row_01) + '>')
                            print(' ')
                            sleep(1)

                    # Write out the row from six loops back as long as
                    # we're at least 6 data-rows into the file (which is actually 7 rows given the header row)
                    if v_rowCounter_coredata2 >= 7:

                        if int(v_parm_flag_loglevel) > 0:
                            print('- unadjusted row : [', str(v_coredata2_row_06), ']')
                            print('  - <' + str(v_coredata2_row_06) + '>')
                            print(' ')
                            sleep(1)

                        # Replace the marker with the actual rolling-average used for safety stock
                        # v_ending_inventory = float(v_f13_value)
                        # v_rolling_safety_stock = float(v_safety_stock_rolling_avg)
                        # v_rolling_safety_stock_mod = float(v_safety_stock_rolling_avg_mod)
                        v_safety_stock_rolling_avg_altered = str(int(float(v_rolling_safety_stock) * v_outcome_fix))

                        v_tmp_string = v_coredata2_row_06.replace("safety_stock_replace_me_01", str(v_rolling_safety_stock) )
                        v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(v_rolling_safety_stock_mod) )
                        v_tmp_string = v_tmp_string.replace("outcome03_replace_me", str(v_safety_stock_rolling_avg_altered) )
                        v_coredata2_row_06 = v_tmp_string

                        if int(v_parm_flag_loglevel) > 0:
                            print('- adjusted row : [', str(v_coredata2_row_06), ']')
                            print('  - <' + str(v_coredata2_row_06) + '>')
                            print(' ')
                            sleep(1)

                        # Convert the string to a JSON value
                        v_current_output_row_json = json.loads(v_coredata2_row_06)

                        # Actually write out the target row
                        v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())

                    # Update the "prior" keyvalue to be "current" keyvalue before the next loop
                    v_keyValue_prior = v_keyValue_current

                    # ==========
                    # = The loop ends here
                    # ==========

            # ---
            # - Write out the remaining few rows that have built up in the FIFO queue
            # ---
            # Row 5
            if v_coredata2_row_05 != "":
                v_tmp_string = v_coredata2_row_05.replace("safety_stock_replace_me_01", str(0))
                v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(0))
                v_tmp_string = v_tmp_string.replace( "outcome03_replace_me", 'OK' )
                v_coredata2_row_05 = v_tmp_string
                v_current_output_row_json = json.loads(v_coredata2_row_05)
                v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())
            # Row 4
            if v_coredata2_row_04 != "":
                v_tmp_string = v_coredata2_row_04.replace("safety_stock_replace_me_01", str(0))
                v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(0))
                v_tmp_string = v_tmp_string.replace( "outcome03_replace_me", 'OK' )
                v_coredata2_row_04 = v_tmp_string
                v_current_output_row_json = json.loads(v_coredata2_row_04)
                v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())
            # Row 3
            if v_coredata2_row_03 != "":
                v_tmp_string = v_coredata2_row_03.replace("safety_stock_replace_me_01", str(0))
                v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(0))
                v_tmp_string = v_tmp_string.replace( "outcome03_replace_me", 'OK' )
                v_coredata2_row_03 = v_tmp_string
                v_current_output_row_json = json.loads(v_coredata2_row_03)
                v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())
            # Row 2
            if v_coredata2_row_02 != "":
                v_tmp_string = v_coredata2_row_02.replace("safety_stock_replace_me_01", str(0))
                v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(0))
                v_tmp_string = v_tmp_string.replace( "outcome03_replace_me", 'OK' )
                v_coredata2_row_02 = v_tmp_string
                v_current_output_row_json = json.loads(v_coredata2_row_02)
                v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())
            # Row 1
            if v_coredata2_row_01 != "":
                v_tmp_string = v_coredata2_row_01.replace("safety_stock_replace_me_01", str(0))
                v_tmp_string = v_tmp_string.replace("safety_stock_replace_me_02", str(0))
                v_tmp_string = v_tmp_string.replace( "outcome03_replace_me", 'OK' )
                v_coredata2_row_01 = v_tmp_string
                v_current_output_row_json = json.loads(v_coredata2_row_01)
                v_csv_file_coredata2_writer.writerow(v_current_output_row_json.values())

# ---
# - Close the file
# ---
# NOTE: auto-closed when using "with open..."


# ---
# - Show total number of MATRIX rows created
# ---
print("\n"*2)
print("Total new coredata2 rows created    : " + str(v_rowCounter_coredata2) )
print("Total unique ITEM-LOC keys processed: " + str(v_keyCounter) )
print("\n"*2)


# ---
# - Display exit message
# ---
v_current_procedure_name = 'Post-Process coredata2: Rolling calculations'
print("==================================================")
print("= " + v_current_procedure_name + ": END")
print("==================================================")
print("\n"*2)
sleep(1)
