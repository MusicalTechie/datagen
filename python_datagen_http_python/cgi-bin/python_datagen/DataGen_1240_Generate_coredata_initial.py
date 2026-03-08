
# ==================================================
# = File:	    DataGen_1240_Generate_orders_initial.py
# = Purpose:	Create initial ORDERS
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - 
# =  - 
# =  -
# = 
# = Dates:
# = ------------------------------------------------
# =  - Created:     2022-JAN-13     Allan Barnard
# =  - Updated:     2022-FEB-24     Allan Barnard, to allow MONTH/WEEK/DAY buckets, Inventory fields, and the beginning of trend-selection options
# =  - Updated:     2022-MAR-31     Allan Barnard, add more forecasting options (intermittent, seasonal, combined)
# =  - Updated:     2022-APR-07     Allan Barnard, perform basic "production" (starting inventory, capacity limits, new production, ending inventory, consumption)
# =  - Updated:     2022-MAY-13     Allan Barnard, add a 3rd field for safety stock (01=raw random generation, 02=improved, 03=pending output from AI/ML engine)
# =  - Updated:     2022-MAY-15     Allan Barnard, add a number of config-file parameters, improve the OUTCOMES (LABELS)
# =  - Updated:     2022-AUG-08     Allan / Colin, add HTML output
# =  - Updated:
# =  - Updated:
# =
# ==================================================

# ---
# - Import Python libraries
# -
# - NOTE: you may have to install these within PyCharm
# -    - Open File > Settings > Project from the PyCharm menu.
# -    - Select your current project.
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
import math

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Full Dataset: Generate COREDATA'




# ---
# - Adding HTML to our AI/ML python code
# ---
print("Content-type: text/html\n")
print("<html>")
print("<title>" + v_current_procedure_name + "</title>")
print("<body bgcolor=#B5CDE1>")
print("<br>")
print("<table border=1 cellspacing=0 cellpadding=8 width=432>")
print(" <tr>")
print("  <td align=center bgcolor=white>")
print("	<b><font size=3>" + v_current_procedure_name + "</font></b>")
print("  </td>")
print(" </tr>")
print("</table>")
print("<br>")
print("<br>")
print("<pre>")


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
v_parm_flag_loglevel=1

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
            print('Parm   : ' + 'v_parm_dg_dmd_trends')
            print('List   : ' + 'v_list_dmd_trends')
            print('Type   : ' + str(type(v_parm_dg_outcome_range)))
            print('Count  : ' + str(len(v_parm_dg_outcome_range)))
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
            print('Parm   : ' + 'v_parm_dg_dmd_trends')
            print('List   : ' + 'v_list_dmd_trends')
            print('Type   : ' + str(type(v_parm_dg_outcome_trigger)))
            print('Count  : ' + str(len(v_parm_dg_outcome_trigger)))
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
            print('Parm   : ' + 'v_parm_dg_dmd_trends')
            print('List   : ' + 'v_list_dmd_trends')
            print('Type   : ' + str(type(v_parm_dg_outcome_fix)))
            print('Count  : ' + str(len(v_parm_dg_outcome_fix)))
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
# - Create a set of COREDATA
# ---
# - Loop through ITEMs in the base file
# -  Loop through LOCATIONS in the base file
# -   Based on the attach-rate variable, assign some ITEMs to LOCATIONs and output in the MATRIX
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    #
    # Set variables
    # Use a preceding "r" to create a "raw" string without any accidental escaped characters like "backslash-b"
    #v_path_locations = r"C:\GitHub_Local_Repository\AIML\AppsAssoc_DEV_DataGen_002_Python-Faker\data_results\base\Master_LOCATIONS.csv"
    # -
    v_path_items            = v_parm_path_items_base
    v_path_customers        = v_parm_path_customers_base
    v_path_matrix           = v_parm_path_matrix_base
    v_path_coredata         = v_parm_path_coredata_base
    # -
    v_fileHandle_items      = ""
    v_fileHandle_locations  = ""
    v_fileHandle_matrix     = ""
    v_fileHandle_coredata   = ""
    # -
    v_rowCounter_items      = 0
    v_rowCounter_locations  = 0
    v_rowCounter_matrix     = 0
    v_rowCounter_period     = 0
    v_rowCounter_coredata   = 0


    # ---
    # - Open COREDATA to WRITE the header (it'll close and re-open continually for appending later)
    # ---
    with open(v_path_coredata, mode='w', newline='') as v_fileHandle_coredata:

        # Create the csv write-object
        v_csv_file_coredata_writer = csv.writer(v_fileHandle_coredata, quoting=csv.QUOTE_ALL)
        v_rowCounter_coredata += 1
        v_current_output_row_json_list = json.loads(v_parm_dg_coredata_col_names)
        v_current_output_row_json_dict = json.loads(v_parm_dg_coredata_col_names)
        #
        # This is odd, but the first JSON.LOAD results in a "LIST" type of variable.
        # The output needs a "DICTIONARY" or true "JSON" type.
        # There are several ways to convert a LIST to a DICT.
        # Since there is only ONE ROW in this LIST, cheating and using a loop to convert to DICT type.
        for v_element in v_current_output_row_json_list:
            v_current_output_row_json_dict = v_element

        v_csv_file_coredata_writer.writerow( v_current_output_row_json_dict.values() )
        # print('-----')
        # print ( "Parameter type: " + str(type(v_parm_dg_coredata_col_names)))
        # print ( "JSON list type: " + str(type(v_current_output_row_json_list)))
        # print ( "JSON list len : " + str(len(v_current_output_row_json_list) ))
        # print ( "JSON dict type: " + str(type(v_current_output_row_json_dict)))
        # print(v_parm_dg_coredata_col_names)
        # print(v_current_output_row_json_list)
        # for v_element in v_current_output_row_json_list:
        #     print("Loop row type   : " + str(type(v_element)))
        #     print("Loop row content: " + str(v_element))


    # ---
    # Reminder of relevant parameters
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
    # - TEST LINE ONLY
    # - If you want to force enable/disable screen-logging "on" temporarily, just comment this line in or out.
    # ---
    # v_parm_flag_loglevel = 0
    v_parm_flag_loglevel = 1

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
    # - Create some variables to hold various algorithm settings
    # ---
    #
    # --- Inventory (fake production: starting inventory, production, ending inventory)
    v_current_inventory_capacity = 0
    v_current_inventory_production = 0
    v_current_inventory_starting = 0
    v_current_inventory_ending = 0
    # ---
    v_prior_inventory_capacity = 0
    v_prior_inventory_production = 0
    v_prior_inventory_starting = 0
    v_prior_inventory_ending = 0
    #
    # --- Intermittent
    v_current_trend_intermittent_chance = 0
    v_current_trend_intermittent_min = 0
    v_current_trend_intermittent_max = 0
    v_current_trend_intermittent_x = 0
    v_current_trend_intermittent_y = 0
    #
    # --- Line
    v_current_trend_line_m = 0
    v_current_trend_line_b = 0
    v_current_trend_line_x = 0
    v_current_trend_line_y = 0
    #
    # --- Seasonal
    # -   presumes a SIN function from 0 to 2pi radians with phase also in 0 to 2pi radians
    # -   presumes that the cycle is annual, in turn based on the select number of periods
    v_current_trend_seasonal_periods_per_year = 0
    v_current_trend_seasonal_phase = 0
    v_current_trend_seasonal_min = 0
    v_current_trend_seasonal_max = 0
    v_current_trend_seasonal_x = 0
    v_current_trend_seasonal_y = 0
    #
    # --- Combined line and seasonal
    # -   presumes use of prior variables
    
    # ---
    # - Final value for "Y" regardless of trend type
    # - The "raw" form is too smooth/predictable to use.
    # - An "altered" form will have a random variance introduced.
    # - 
    v_current_calculated_volume_raw = 0
    v_current_calculated_volume_altered = 0

    # ---
    # - Create CALENDAR objects (e.g., HISTORY, PRESENT, FUTURE)
    # ---

    # -
    # The "date_range" function has different strings to determine various forms of month, week, or other periods to use.
    # Set this string into a variable that varies with the "bucket type"
    # -
    # ---
    v_parm_current = "DG_PERIOD_TYPE"
    v_parm_dg_period_type_incr_str = 'MS'
    v_temp_val = ""
    if (v_parm_dg_period_type == "MONTH"):
        v_temp_val = "MS"
        v_current_trend_seasonal_periods_per_year = 12
    elif (v_parm_dg_period_type == "WEEK"):
        # Form the string from "W-" and the first three letters of the DAY-OF-WEEK
        v_temp_val = "W" + "-" + v_parm_dg_period_start_dow[0:3]
        v_current_trend_seasonal_periods_per_year = 52
    elif (v_parm_dg_period_type == "DAY"):
        v_temp_val = "D"
        v_current_trend_seasonal_periods_per_year = 365
    else:
        # default to MONTH
        v_temp_val = "MS"
    v_parm_dg_period_type_incr_str = v_temp_val


    # -
    # History range (commonly known as "open" orders) (typically it is slightly in the past and slightly in the future)
    # -
    v_temp_date_start = v_date_history_start.strftime('%m-%d-%Y')
    v_temp_date_end = v_date_history_end.strftime('%m-%d-%Y')
    v_list_dates_history = pandas.date_range( start=v_temp_date_start, end=v_temp_date_end, freq=v_parm_dg_period_type_incr_str)
    if 1 == 2:
        print('-----')
        print("Start: " + v_temp_date_start )
        print("End  : " + v_temp_date_end )
        print( v_list_dates_history )

    # -
    # Open-Order range (commonly known as "open" orders) (typically it is slightly in the past and slightly in the future)
    # -
    v_temp_date_start = v_date_openorders_start.strftime('%m-%d-%Y')
    v_temp_date_end = v_date_openorders_end.strftime('%m-%d-%Y')
    v_list_dates_openorders = pandas.date_range( start=v_temp_date_start, end=v_temp_date_end, freq=v_parm_dg_period_type_incr_str)
    if 1 == 2:
        print('-----')
        print("Start: " + v_temp_date_start )
        print("End  : " + v_temp_date_end )
        print( v_list_dates_openorders )

    # -
    # Future range (commonly known as "open" orders) (typically it is slightly in the past and slightly in the future)
    # -
    v_temp_date_start = v_date_future_start.strftime('%m-%d-%Y')
    v_temp_date_end = v_date_future_end.strftime('%m-%d-%Y')
    v_list_dates_future = pandas.date_range( start=v_temp_date_start, end=v_temp_date_end, freq=v_parm_dg_period_type_incr_str)
    if 1 == 2:
        print('-----')
        print("Start: " + v_temp_date_start )
        print("End  : " + v_temp_date_end )
        print( v_list_dates_future )


    # ---
    # - Open MATRIX for READ
    # ---
    with open(v_path_matrix, mode='r') as v_fileHandle_matrix:

        # Create the csv read-object
        v_csv_file_matrix_reader = csv.reader(v_fileHandle_matrix)

        # ---
        # - Loop through ITEM-LOC combinations in the MATRIX file and generate
        # - both HISTORY and FUTURE values.
        # ---
        # NOTE: these particular rows are "value only" and will read as "LIST" objects rather than "DICTIONARY" objects
        for v_row_matrix in v_csv_file_matrix_reader:
            
            # Count the matrix rows processed (not including the header)
            v_rowCounter_matrix += 1
            v_tempstr = str(v_rowCounter_matrix)

            # Restart the period counter for each new combination (each matrix row)
            v_rowCounter_period = 1


            # ---
            # - Only process if past the first row (header)
            # ---
            if v_rowCounter_matrix > 1:

                # -
                # - Pick a random trend for this combination of ITEM and LOCATION
                # -
                # - NOTE: you have to pull out the "value" portion of the list element that corresponds with "TrendName"
                # -       as noted in the config file.  The raw element of the list will appear as: {'DTRowID': '201', 'TrendName': 'Slope01'}
                # -
                v_temp_rnd = random.randint(0, int(v_parm_dg_num_dmd_trends)-1 )
                v_current_trend_type = str(v_list_dmd_trends[v_temp_rnd])
                # print (str(v_current_trend_type))

                # -
                # - While determining the trend, pick a value a few years out
                # - into the trend and use that as the "capacity".  This will
                # - ensure some "ending inventory" values are too high to start
                # - with and to low later.
                # -
                # - Set it to zero here... then update it depending on the trend chosen.
                v_current_inventory_capacity = 0

                # -
                # - Create random factors relevant to the selected trend type
                # -
                if (v_current_trend_type.find("Intermittent01") > -1 ):

                    v_trend_type_to_save_in_file = "Intermittent01"
                    # NOTE: can set this as a degree of intermittent activity... perhaps "X" number of random periods generate "Y1 to Y2" quantity

                    # --- Intermittent
                    v_current_trend_intermittent_chance = random.randint(1, 10)
                    v_current_trend_intermittent_min = random.randint(1, 50) * 10
                    v_current_trend_intermittent_max = v_current_trend_intermittent_min + random.randint(1, 50) * 10
                    v_current_trend_intermittent_x = v_rowCounter_period

                    # Note that a chance of 1-10 that is <2 means "it's 1".  So when the random number is 1 out of 10, save a random volume.
                    if (v_current_trend_intermittent_chance < 2):
                        v_current_trend_intermittent_y = random.randint(v_current_trend_intermittent_min, v_current_trend_intermittent_max )
                    else:
                        v_current_trend_intermittent_y = 0

                    # Set overall value for volume (regardless of method used)
                    v_current_calculated_volume_altered = v_current_trend_intermittent_y

                    # Set production capacity to a representative value
                    v_current_inventory_capacity = random.randint(v_current_trend_intermittent_min, v_current_trend_intermittent_max )

                elif (v_current_trend_type.find("Slope01") > -1 ):

                    v_trend_type_to_save_in_file = "Slope01"

                    # NOTE: we could improve this over time to include a range for slope and a range in min/max value
                    #       (would have to add new parameters to the config file)

                    # Line: y=mx+b
                    v_current_trend_line_m = random.randint(1, 10) * 10
                    v_current_trend_line_b = random.randint(1, 1000)
                    v_current_trend_line_x = v_rowCounter_period
                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                    # Set overall value for volume (regardless of method used)
                    v_current_calculated_volume_raw = v_current_trend_line_y

                    # Set production capacity to a representative value about 3 years out from the starting point
                    v_capacity_estimate_x_value = v_current_trend_seasonal_periods_per_year * 3
                    v_current_inventory_capacity = (v_current_trend_line_m * v_capacity_estimate_x_value) + v_current_trend_line_b


                elif (v_current_trend_type.find("Seasonal01") > -1 ):

                    v_trend_type_to_save_in_file = "Seasonal01"
                    # NOTE: Can set this to a COSINE or SINE function with a "y intercept", an amplitude, and a phase-offset

                    # --- Seasonal
                    # -   phase is a random number from 0 to 2 (as in 0pi to 2pi)
                    v_current_trend_seasonal_phase = random.random() * 2
                    v_current_trend_seasonal_min = random.randint(1, 250)
                    v_current_trend_seasonal_max = v_current_trend_seasonal_min + random.randint(1,250)
                    v_current_trend_seasonal_x = v_rowCounter_period / (v_current_trend_seasonal_periods_per_year/2)
                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin( (v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi) )

                    # Set overall value for volume (regardless of method used)
                    v_current_calculated_volume_raw = v_current_trend_seasonal_y

                    # Set production capacity to a representative value about 3 years out from the starting point
                    v_capacity_estimate_x_value = v_current_trend_seasonal_periods_per_year * 3
                    v_current_inventory_capacity = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin( (v_capacity_estimate_x_value + v_current_trend_seasonal_phase) * math.pi) )

                elif (v_current_trend_type.find("Combined01") > -1 ):

                    v_trend_type_to_save_in_file = "Combined01"

                    # Line: y=mx+b
                    v_current_trend_line_m = random.randint(1, 10) * 10
                    v_current_trend_line_b = random.randint(1, 1000)
                    v_current_trend_line_x = v_rowCounter_period
                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                    # --- Seasonal
                    # -   phase is a random number from 0 to 2 (as in 0pi to 2pi)
                    # ---
                    v_current_trend_seasonal_phase = random.random() * 2
                    v_current_trend_seasonal_min = random.randint(1, 250)
                    v_current_trend_seasonal_max = v_current_trend_seasonal_min + random.randint(1,250)
                    v_current_trend_seasonal_x = v_rowCounter_period / (v_current_trend_seasonal_periods_per_year/2)
                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin( (v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi) )

                    # Set overall value for volume (regardless of method used)
                    v_current_calculated_volume_raw = v_current_trend_line_y + v_current_trend_seasonal_y

                    # Set production capacity to a representative value about 3 years out from the starting point
                    v_capacity_estimate_x_value = v_current_trend_seasonal_periods_per_year * 3
                    v_current_inventory_capacity_line = (v_current_trend_line_m * v_capacity_estimate_x_value) + v_current_trend_line_b
                    v_current_inventory_capacity_seasonal = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin( (v_capacity_estimate_x_value + v_current_trend_seasonal_phase) * math.pi) )
                    v_current_inventory_capacity = v_current_inventory_capacity_line + v_current_inventory_capacity_seasonal

                else:
                    # Default to a line
                    v_current_trend_line_m = random.randint(1, 10) * 10
                    v_current_trend_line_b = random.randint(1, 1000)
                    v_current_trend_line_x = v_rowCounter_period
                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b
                    v_current_calculated_volume_raw = v_current_trend_seasonal_y

                    # Set production capacity to a representative value about 3 years out from the starting point
                    v_capacity_estimate_x_value = v_current_trend_seasonal_periods_per_year * 3
                    v_current_inventory_capacity = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin( (v_capacity_estimate_x_value + v_current_trend_seasonal_phase) * math.pi) )

                # -
                # - Pick a random production-capacity for this combination
                # -
                # - NOTE: production capacity should likely be PER-ITEM unless each of these combinations is a manufacturing location
                # -
                # - NOTE: we could add multiple production-lines per ITEM or per ITEM-LOCATION combination and add a
                #         capacity for each in the config file.
                # -
                # - NOTE: capacity has to have some correlation to typical demand; if they're too far off then
                # -       you'll get either massive ending inventories or zero (or negative) ending inventories.
                # -       For now, using a point in the curve that is out a few years from the starting point
                # -
                # -

                # These values are in the config file as of 2022-May-15
                # v_parm_dg_prod_capacity_min, v_parm_dg_prod_capacity_max, v_parm_dg_prod_capacity_round
                v_minimum_capacity = int(v_parm_dg_prod_capacity_min)
                v_factor_rounding = int(v_parm_dg_prod_capacity_round)

                # initial capacity was calculated prior during the trend calculations
                # print('Capacity 1: [' + str(v_current_inventory_capacity) + ']')

                # adjust to be at least at minimum capacity
                # otherwise, calculate a value between the minimum and maximum (from the config file)
                if v_current_inventory_capacity < v_minimum_capacity:
                    v_current_inventory_capacity = random.randint( int(v_parm_dg_prod_capacity_min), int(v_parm_dg_prod_capacity_max) )

                # print('Capacity 2: [' + str(v_current_inventory_capacity) + ']')

                # Round to a desired number of digits (based on the config file)
                v_current_inventory_capacity = round(v_current_inventory_capacity / v_factor_rounding) * v_factor_rounding

                # print('Capacity 3: [' + str(v_current_inventory_capacity) + ']')
                # print(' ')
                # sleep(5)


                # ---
                # - Open the target file and loop through various CALENDAR "lists" and generate data
                # -
                # - Skip the first row (header row).
                # ---
                if v_rowCounter_matrix > 1:
                    with open(v_path_coredata, mode='a+', newline='') as v_fileHandle_coredata:
                        #
                        # Create the csv write-object
                        v_csv_file_coredata_writer = csv.writer(v_fileHandle_coredata, quoting=csv.QUOTE_ALL)

                        # ---
                        # - Reset the rowCounter to "0" " right before the calendar loop(s)
                        # - so that the auto-increment at the top of the loop will bring
                        # - the value to "1".
                        # ---
                        v_rowCounter_period =0

                        # ---
                        # - Loop through the HISTORY CALENDAR list and generate data (but skip first header row of the MATRIX file)
                        # ---
                        if 1 == 1:
                            for v_current_date_element in v_list_dates_history:

                                # Increment the period counter (which will act as the "x" coordinate in calculations)
                                v_rowCounter_period += 1

                                # -
                                # - Update the "y" calculation (volume) based on the prior-chosen trend type
                                # -
                                if (v_trend_type_to_save_in_file == "Intermittent01"):

                                    v_current_trend_intermittent_chance = random.randint(1, 10)
                                    if (v_current_trend_intermittent_chance <= 3):
                                        v_current_trend_intermittent_y = random.randint(v_current_trend_intermittent_min,v_current_trend_intermittent_max)
                                    else:
                                        v_current_trend_intermittent_y = 0

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_intermittent_y

                                elif (v_trend_type_to_save_in_file == "Slope01"):

                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_line_y

                                elif (v_trend_type_to_save_in_file == "Seasonal01"):

                                    v_current_trend_seasonal_x = v_rowCounter_period / (
                                                v_current_trend_seasonal_periods_per_year / 2)
                                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin((v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi))

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_seasonal_y

                                elif (v_trend_type_to_save_in_file == "Combined01"):

                                    # Line: y=mx+b
                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                                    # --- Seasonal
                                    v_current_trend_seasonal_x = v_rowCounter_period / (v_current_trend_seasonal_periods_per_year / 2)
                                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin((v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi))

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_line_y + v_current_trend_seasonal_y

                                else:
                                    # Default to a line
                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b
                                    v_current_calculated_volume_raw = v_current_trend_seasonal_y

                                # -
                                # - Add some variation to the calculated volume... so it is NOT PERFECT
                                # -
                                # print('Type v_parm_dg_dmd_fc_variance      : ' + str(type(v_parm_dg_dmd_fc_variance)))
                                # print('Type v_current_calculated_volume_raw: ' + str(type(v_current_calculated_volume_raw)))
                                #
                                v_temp_x = float(v_parm_dg_dmd_fc_variance)
                                v_temp_y = int(v_temp_x)
                                v_variance_range = int( v_temp_y * v_current_calculated_volume_raw )
                                v_variance_volume = random.randint( -1 * v_variance_range, v_variance_range)
                                v_current_calculated_volume_altered = v_current_calculated_volume_raw + v_variance_volume


                                # ==========
                                # -
                                # Compose the COREDATA columns for the past (HISTORY)
                                # -
                                # ==========

                                # - F01
                                v_f01_name  = "Period"
                                v_temp_val = v_current_date_element.strftime("%Y-%m-%d")
                                v_f01_value = v_temp_val

                                # - F02
                                v_f02_name  = "Item"
                                v_f02_value = v_row_matrix[0]

                                # - F03
                                v_f03_name = "Location"
                                v_f03_value = v_row_matrix[1]

                                # - F04
                                v_f04_name  = "Orders_Complete"
                                v_temp_val = v_current_calculated_volume_altered
                                v_f04_value = str(v_temp_val)

                                # - F05
                                v_f05_name  = "Orders_Open"
                                v_temp_rnd = random.randint(1, 50)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f05_value = str(v_temp_val)

                                # - F06
                                v_f06_name = "Orders_Cancelled"
                                v_temp_rnd = random.randint(1, 5)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f06_value = str(v_temp_val)

                                # - F07
                                v_f07_name = "Orders_Returned"
                                v_temp_rnd = random.randint(1, 5)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f07_value = str(v_temp_val)

                                # - F08
                                v_f08_name = "Orders_Forecast01"
                                # Vary the "variance" based on the size of the completed order volume (currently 10%, or 0.10)
                                v_forecast_variance = int(float(v_parm_dg_dmd_fc_variance) * v_current_calculated_volume_altered)
                                v_temp_rnd = random.randint( -1 * v_forecast_variance, v_forecast_variance)
                                v_temp_val = str(v_temp_rnd)
                                v_temp_val = v_current_calculated_volume_altered + v_temp_rnd
                                if v_temp_val < 0:
                                        v_temp_val = 0
                                v_f08_value = str(v_temp_val)

                                # - F09
                                v_f09_name = "Orders_Forecast02"
                                v_temp_rnd = random.randint(1, 50)
                                v_temp_val = str(v_temp_rnd)
                                v_f09_value = str(0)

                                # -
                                # -
                                # - NOTE: fields 14/15/16 have been moved here as their
                                # -       values are used by inventory calculations.
                                # -

                                # - F14
                                # - This is a shot-in-the-dark at generating a first safety-stock with some broad but reasonable limits
                                # - Create safety stock variations based on ORDERS and on CAPACITY
                                # - Choose whichever is lower (this limits safety stock to a multiple of capacity)
                                v_f14_name = "SafetyStock01"
                                v_temp_val1 = v_current_calculated_volume_altered * float(v_parm_dg_dmd_ss_factor)
                                v_temp_val2 = v_current_inventory_capacity * float(v_parm_dg_dmd_ss_factor)
                                v_temp_val3 = v_temp_val1
                                if v_temp_val1 > v_temp_val2:
                                    v_temp_val3 = v_temp_val2
                                v_f14_value = str(v_temp_val3)

                                # - F15
                                # - This value will be calculated in the NEXT script that calculates
                                #   a rolling-average safety stock and calculates production and ending-inventory.
                                # - This will be a "corrected" safety stock suitable for submission to the AI/ML engine.
                                v_f15_name = "SafetyStock02"
                                v_temp_val = 0
                                v_f15_value = str(v_temp_val)

                                # - F16
                                # - This is expected to be populated as primary output from the AI/ML engine
                                v_f16_name = "SafetyStock03"
                                v_temp_val = 0
                                v_f16_value = str(v_temp_val)

                                # - F10
                                v_f10_name = "Inventory_starting"
                                # Update the starting inventory from the last period unless this is the first period
                                if (v_rowCounter_period > 1):
                                    v_current_inventory_starting = float(v_prior_inventory_ending)
                                else:
                                    v_current_inventory_starting = float(0)
                                #
                                # Make sure starting inventory is not negative
                                if v_current_inventory_starting < 0:
                                    v_current_inventory_starting = float(0)
                                #
                                v_temp_val = str(v_current_inventory_starting)
                                v_f10_value = str(v_temp_val)

                                # - F11
                                v_f11_name = "Inventory_capacity"
                                v_temp_val = v_current_inventory_capacity
                                v_f11_value = str(v_temp_val)

                                # - F12
                                v_f12_name = "Inventory_production"
                                # NOTE: this will have to be improved to reflect number-of-production-lines, variable
                                #       capacities per-item-per-line, etc.
                                # WARNING: in this simple calculation it is possible for safety-stock to exceed capacity
                                #
                                # Calculate the initial value of production (random)
                                v_temp_rnd = random.randint(1, v_current_inventory_capacity)
                                v_current_inventory_production = float(v_temp_rnd)
                                #
                                # Then calculate the greater of "orders completed" and "forecast"
                                v_temp_orders = float(v_f04_value)
                                v_temp_forecast = float(v_f08_value)
                                v_temp_requirement = v_temp_orders
                                if v_temp_forecast > v_temp_orders:
                                    v_temp_requirement = v_temp_forecast
                                #
                                # Then do a quick check to see what our likely ending-inventory might be (StartInv + Requirement - OrdersCompleted)
                                v_temp_starting_inventory = float(v_f10_value)
                                v_temp_projected_ending_inventory = (v_temp_starting_inventory + v_temp_requirement) - v_temp_orders
                                #
                                # If the projected ending-inventory is less than safety stock, then add the difference to production
                                v_temp_safety_stock = float(v_f14_value)
                                if v_temp_projected_ending_inventory < v_temp_safety_stock:
                                    v_temp_difference = v_temp_safety_stock - v_temp_projected_ending_inventory
                                    v_current_inventory_production = v_current_inventory_production + v_temp_difference
                                    v_temp_projected_ending_inventory = v_temp_safety_stock
                                #
                                # If the projected ending-inventory is more than some factor of the "orders-completed" then
                                # cap the production value.  Can't just keep producing more inventory with no constraints.
                                v_temp_max_inventory_factor = 3
                                if v_temp_projected_ending_inventory > (v_temp_orders * v_temp_max_inventory_factor):
                                    v_temp_difference = v_temp_projected_ending_inventory - (
                                                v_temp_orders * v_temp_max_inventory_factor)
                                    v_current_inventory_production = v_current_inventory_production - v_temp_difference
                                    v_temp_projected_ending_inventory = (v_temp_orders * v_temp_max_inventory_factor)
                                #
                                # Ensure that inventory is not a negative value.  This will be set to zero.
                                # This is essentially a "fill or kill" scenario; missed orders are not carried foreward.
                                if float(v_current_inventory_production) < float(0):
                                    v_current_inventory_production = float(0)
                                #
                                v_temp_val = str(v_current_inventory_production)
                                v_f12_value = str(v_temp_val)

                                # - F13
                                v_f13_name = "Inventory_end"
                                #
                                # Ending inventory includes simple consumption (starting, + production, -orders_completed)
                                # Later, this could include all the orders variants (e.g. Cancelled, returned).
                                # See the NOTE comments at the point where the trends are selected... lots of improvement
                                # possible for inventory capacity, production, and consumption.
                                v_temp_val = float(v_current_inventory_starting) + float(v_current_inventory_production) - float(v_f04_value)
                                #
                                # Make sure that ending inventory isn't negative
                                #
                                # Make sure starting inventory is not negative
                                if v_temp_val < 0:
                                    v_temp_val = float(0)
                                #
                                # Use the opportunity to set the "prior" value in preparation for the NEXT record in the loop
                                v_prior_inventory_ending = v_temp_val
                                #
                                v_f13_value = str(v_temp_val)

                                # - F14, F15, F16 moved earlier in this script

                                # - F17
                                v_f17_name = "Net_Requirement"
                                #
                                # Can be greater-of-orders-or-forecast, plus (difference between greater-of-StartInv-and-zero and SafetyStock)
                                v_temp_val = float(v_f04_value)
                                #
                                # Check to see if the forecast is larger than the orders_completed... use forecast if this is true
                                if v_temp_val < float(v_f08_value):
                                    v_temp_val = float(v_f08_value)
                                #
                                # Subtract starting inventory
                                v_temp_val = v_temp_val - float(v_f10_value)
                                #
                                # If v_temp_val is less than zero, make it zero
                                if v_temp_val < float(0):
                                    v_temp_val = float(0)
                                #
                                # if v_temp_val is less than safety-stock, make it safety-stock
                                if v_temp_val < float(v_f14_value):
                                    v_temp_val = float(v_f14_value)
                                #
                                # WARNING: Yes, this is an incomplete/incorrect net-requirements calc.
                                #          But, it will be corrected in the rolling functions of COREDATA2
                                v_f17_value = str(v_temp_val)

                                # - F18
                                # - Determine an initial label value
                                # - Then make an effort to convert that to a corrective value
                                # - Then set a new and hopefully improved safety stock value.
                                # - parameter values: v_parm_dg_outcome_range, v_parm_dg_outcome_trigger, v_parm_dg_outcome_fix
                                    #
                                    # Example:
                                    #  DG_OUTCOME_RANGE   = [{"Field01": "VeryLow", "Field02": "Low", "Field03": "OK", "Field04": "High","Field05": "VeryHigh"}]
                                    #  DG_OUTCOME_TRIGGER = [{"Field01": ".50", "Field02": ".75", "Field03": "1.00", "Field04": "1.25","Field05": "1.50"}]
                                    #  DG_OUTCOME_FIX	  = [{"Field01": "1.50", "Field02": "1.25", "Field03": "1.00", "Field04": ".75", "Field05": ".50"}]

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

                                v_f18_name = "Outcome01"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = int(v_temp_rnd)
                                #
                                # Temporarily set this to NULL... it will be fixed in the next script
                                #
                                v_temp_val=""
                                    # if (v_temp_rnd <= 40):
                                    #     v_temp_val = "Worse"
                                    # elif (v_temp_rnd <= 80):
                                    #     v_temp_val = "Better"
                                    # else:
                                    #     v_temp_val = "Indeterminate"
                                v_f18_value = str(v_temp_val)

                                # - F19
                                v_f19_name = "Outcome02"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = ""
                                # if (v_temp_rnd <= 40):
                                #     v_temp_val = "Worse"
                                # elif (v_temp_rnd <= 80):
                                #     v_temp_val = "Better"
                                # else:
                                #     v_temp_val = "Indeterminate"
                                v_temp_val = ""
                                v_f19_value = str(v_temp_val)

                                # - F20
                                v_f20_name = "Outcome03"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = ""
                                # if (v_temp_rnd <= 40):
                                #     v_temp_val = "Worse"
                                # elif (v_temp_rnd <= 80):
                                #     v_temp_val = "Better"
                                # else:
                                #     v_temp_val = "Indeterminate"
                                v_f20_value = str(v_temp_val)

                                # - F21
                                v_f21_name = "Trend_type"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = v_trend_type_to_save_in_file
                                v_f21_value = str(v_temp_val)

                                # - F22
                                v_f22_name = "Trend_factor1"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_chance
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = v_current_trend_line_m
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_line_m
                                else:
                                    # Default to a line
                                    v_temp_val = v_current_trend_line_m
                                v_f22_value = str(v_temp_val)

                                # - F23
                                v_f23_name = "Trend_factor2"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_min
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = v_current_trend_line_b
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_line_b
                                else:
                                    # Default to a line
                                    v_temp_val = v_current_trend_line_b
                                v_f23_value = str(v_temp_val)

                                # - F24
                                v_f24_name = "Trend_factor3"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_max
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_phase
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_phase
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f24_value = str(v_temp_val)

                                # - F25
                                v_f25_name = "Trend_factor4"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_min
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_min
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f25_value = str(v_temp_val)

                                # - F26
                                v_f26_name = "Trend_factor5"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_max
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_max
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f26_value = str(v_temp_val)

                                # - F27
                                v_f27_name = "Last_Period"
                                v_temp_val = v_current_date_element.strftime("%Y-%m-%d")
                                v_f27_value = str(v_temp_val)

                                # - F28
                                v_f28_name = "Last_X_Value"
                                v_temp_val = v_rowCounter_period
                                v_f28_value = str(v_temp_val)

                                # - F29
                                v_f29_name = "Last_Y_Value"
                                v_temp_val = v_current_calculated_volume_raw
                                v_f29_value = str(v_temp_val)


                                # -
                                # - Write the entire record to the target file
                                # -
                                v_current_output_row = '{ ' +   '"' + v_f01_name + '"' + ": " + '"' + v_f01_value + '"' \
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
                                                            + ', "' + v_f15_name + '"' + ": " + '"' + v_f15_value + '"' \
                                                            + ', "' + v_f16_name + '"' + ": " + '"' + v_f16_value + '"' \
                                                            + ', "' + v_f17_name + '"' + ": " + '"' + v_f17_value + '"' \
                                                            + ', "' + v_f18_name + '"' + ": " + '"' + v_f18_value + '"' \
                                                            + ', "' + v_f19_name + '"' + ": " + '"' + v_f19_value + '"' \
                                                            + ', "' + v_f20_name + '"' + ": " + '"' + v_f20_value + '"' \
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

                                # Update the number of records added to the output file
                                v_rowCounter_coredata += 1

                                # Convert the string to a JSON value
                                v_current_output_row_json = json.loads(v_current_output_row)

                                # Write out the result in CSV format
                                v_csv_file_coredata_writer.writerow(v_current_output_row_json.values())

                                if 1 == 2:
                                    print('-----')
                                    v_tempstr = str(v_rowCounter_matrix)
                                    print(v_tempstr.rjust(3,'0') + ", ", end = "")
                                    print(str(type(v_current_output_row)) + ", ", end = "")
                                    print(v_current_output_row)
                                    print(v_current_date_element.strftime("%Y-%m-%d"))

                        # ---
                        # - Loop through the FUTURE CALENDAR list and generate data (but skip first header row of the MATRIX file)
                        # - REMINDER: the "current" period is included in the FUTURE periods so it doesn't have to be generated separately
                        # ---
                        if 1 == 1:
                            for v_current_date_element in v_list_dates_future:

                                # Increment the period counter (which will act as the "x" coordinate in calculations)
                                v_rowCounter_period += 1

                                # -
                                # - Update the "y" calculation (volume) based on the prior-chosen trend type
                                # -
                                if (v_trend_type_to_save_in_file == "Intermittent01"):

                                    v_current_trend_intermittent_chance = random.randint(1, 10)
                                    if (v_current_trend_intermittent_chance <= 3):
                                        v_current_trend_intermittent_y = random.randint(v_current_trend_intermittent_min,v_current_trend_intermittent_max)
                                    else:
                                        v_current_trend_intermittent_y = 0

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_intermittent_y

                                elif (v_trend_type_to_save_in_file == "Slope01"):

                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_line_y

                                elif (v_trend_type_to_save_in_file == "Seasonal01"):

                                    v_current_trend_seasonal_x = v_rowCounter_period / (
                                                v_current_trend_seasonal_periods_per_year / 2)
                                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin((v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi))

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_seasonal_y

                                elif (v_trend_type_to_save_in_file == "Combined01"):

                                    # Line: y=mx+b
                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b

                                    # --- Seasonal
                                    v_current_trend_seasonal_x = v_rowCounter_period / (v_current_trend_seasonal_periods_per_year / 2)
                                    v_current_trend_seasonal_y = (v_current_trend_seasonal_min + v_current_trend_seasonal_max) + (v_current_trend_seasonal_max * math.sin((v_current_trend_seasonal_x + v_current_trend_seasonal_phase) * math.pi))

                                    # Set overall value for volume (regardless of method used)
                                    v_current_calculated_volume_raw = v_current_trend_line_y + v_current_trend_seasonal_y

                                else:
                                    # Default to a line
                                    v_current_trend_line_x = v_rowCounter_period
                                    v_current_trend_line_y = (v_current_trend_line_m * v_current_trend_line_x) + v_current_trend_line_b
                                    v_current_calculated_volume_raw = v_current_trend_seasonal_y


                                # -
                                # - Add some variation to the calculated volume... so it is NOT PERFECT
                                # -
                                v_variance_range = int(.20 * v_current_calculated_volume_raw)
                                v_variance_volume = random.randint( -1 * v_variance_range, v_variance_range)
                                v_current_calculated_volume_altered = v_current_calculated_volume_raw + v_variance_volume


                                # ==========
                                # -
                                # Compose the COREDATA columns for the future (FORECAST)
                                # -
                                # ==========

                                # - F01
                                v_f01_name  = "Period"
                                v_temp_val = v_current_date_element.strftime("%Y-%m-%d")
                                v_f01_value = v_temp_val

                                # - F02
                                v_f02_name  = "Item"
                                v_f02_value = v_row_matrix[0]

                                # - F03
                                v_f03_name = "Location"
                                v_f03_value = v_row_matrix[1]

                                # - F04
                                v_f04_name  = "Orders_Complete"
                                v_temp_val = 0
                                v_f04_value = str(v_temp_val)

                                # - F05
                                v_f05_name  = "Orders_Open"
                                v_temp_rnd = random.randint(1, 50)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f05_value = str(v_temp_val)

                                # - F06
                                v_f06_name = "Orders_Cancelled"
                                v_temp_rnd = random.randint(1, 5)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f06_value = str(v_temp_val)

                                # - F07
                                v_f07_name = "Orders_Returned"
                                v_temp_rnd = random.randint(1, 5)
                                if ( v_current_date_element.strftime("%Y-%m-%d") >= v_parm_dg_date_openorders_start ):
                                    v_temp_val = 0
                                else:
                                    v_temp_val = str(v_temp_rnd)
                                v_f07_value = str(v_temp_val)

                                # - F08
                                v_f08_name = "Orders_Forecast01"
                                # Vary the "variance" based on the size of the completed order volume (currently 10%, or 0.10)
                                v_forecast_variance = int(.30 * v_current_calculated_volume_altered)
                                v_temp_rnd = random.randint( -1 * v_forecast_variance, v_forecast_variance)
                                v_temp_val = str(v_temp_rnd)
                                v_temp_val = v_current_calculated_volume_altered + v_temp_rnd
                                if v_temp_val < 0:
                                        v_temp_val = 0
                                v_f08_value = str(v_temp_val)

                                # - F09
                                v_f09_name = "Orders_Forecast02"
                                v_temp_rnd = random.randint(1, 50)
                                v_temp_val = str(v_temp_rnd)
                                v_f09_value = str(0)

                                # -
                                # -
                                # - NOTE: fields 14/15/16 have been moved here as their
                                # -       values are used by inventory calculations.
                                # -

                                # - F14
                                # - Create safety stock variations based on ORDERS and on CAPACITY
                                # - Choose whichever is lower (this limits safety stock to a multiple of capacity)
                                v_f14_name = "SafetyStock01"
                                v_temp_val1 = v_current_calculated_volume_altered * float(v_parm_dg_dmd_ss_factor)
                                v_temp_val2 = v_current_inventory_capacity * float(v_parm_dg_dmd_ss_factor)
                                v_temp_val3 = v_temp_val1
                                if v_temp_val1 > v_temp_val2:
                                    v_temp_val3 = v_temp_val2
                                v_f14_value = str(v_temp_val3)

                                # - F15
                                v_f15_name = "SafetyStock02"
                                v_temp_val = 0
                                v_f15_value = str(v_temp_val)

                                # - F16
                                v_f16_name = "SafetyStock03"
                                v_temp_val = 0
                                v_f16_value = str(v_temp_val)

                                # - F10
                                v_f10_name = "Inventory_starting"
                                # Update the starting inventory from the last period unless this is the first period
                                if (v_rowCounter_period > 1):
                                    v_current_inventory_starting = float(v_prior_inventory_ending)
                                else:
                                    v_current_inventory_starting = float(0)
                                #
                                # Make sure starting inventory is not negative
                                if v_current_inventory_starting < 0:
                                    v_current_inventory_starting = float(0)
                                #
                                v_temp_val = str(v_current_inventory_starting)
                                v_f10_value = str(v_temp_val)

                                # - F11
                                v_f11_name = "Inventory_capacity"
                                v_temp_val = v_current_inventory_capacity
                                v_f11_value = str(v_temp_val)

                                # - F12
                                v_f12_name = "Inventory_production"
                                # NOTE: this will have to be improved to reflect number-of-production-lines, variable
                                #       capacities per-item-per-line, etc.
                                # WARNING: in this simple calculation it is possible for safety-stock to exceed capacity
                                #
                                # Calculate the initial value of production (random)
                                v_temp_rnd = random.randint(1, v_current_inventory_capacity)
                                v_current_inventory_production = float(v_temp_rnd)
                                #
                                # Then calculate the greater of "orders completed" and "forecast"
                                v_temp_orders = float(v_f04_value)
                                v_temp_forecast = float(v_f08_value)
                                v_temp_requirement = v_temp_orders
                                if v_temp_forecast > v_temp_orders:
                                    v_temp_requirement = v_temp_forecast
                                #
                                # Then do a quick check to see what our likely ending-inventory might be (StartInv + Requirement - OrdersCompleted)
                                v_temp_starting_inventory = float(v_f10_value)
                                v_temp_projected_ending_inventory = (v_temp_starting_inventory + v_temp_requirement) - v_temp_orders
                                #
                                # If the projected ending-inventory is less than safety stock, then add the difference to production
                                v_temp_safety_stock = float(v_f14_value)
                                if v_temp_projected_ending_inventory < v_temp_safety_stock:
                                    v_temp_difference = v_temp_safety_stock - v_temp_projected_ending_inventory
                                    v_current_inventory_production = v_current_inventory_production + v_temp_difference
                                    v_temp_projected_ending_inventory = v_temp_safety_stock
                                #
                                # If the projected ending-inventory is more than some factor of the "orders-completed" then
                                # cap the production value.  Can't just keep producing more inventory with no constraints.
                                v_temp_max_inventory_factor = 3
                                if v_temp_projected_ending_inventory > (v_temp_orders * v_temp_max_inventory_factor):
                                    v_temp_difference = v_temp_projected_ending_inventory - (
                                                v_temp_orders * v_temp_max_inventory_factor)
                                    v_current_inventory_production = v_current_inventory_production - v_temp_difference
                                    v_temp_projected_ending_inventory = (v_temp_orders * v_temp_max_inventory_factor)
                                #
                                # Ensure that inventory is not a negative value.  This will be set to zero.
                                # This is essentially a "fill or kill" scenario; missed orders are not carried foreward.
                                if float(v_current_inventory_production) < float(0):
                                    v_current_inventory_production = float(0)
                                #
                                v_temp_val = str(v_current_inventory_production)
                                v_f12_value = str(v_temp_val)

                                # - F13
                                v_f13_name = "Inventory_end"
                                #
                                # Ending inventory includes simple consumption (starting, + production, -orders_completed)
                                # Later, this could include all the orders variants (e.g. Cancelled, returned).
                                # See the NOTE comments at the point where the trends are selected... lots of improvement
                                # possible for inventory capacity, production, and consumption.
                                v_temp_val = float(v_current_inventory_starting) + float(v_current_inventory_production) - float(v_f04_value)
                                #
                                # Make sure that ending inventory isn't negative
                                #
                                # Make sure starting inventory is not negative
                                if v_temp_val < 0:
                                    v_temp_val = float(0)
                                #
                                # Use the opportunity to set the "prior" value in preparation for the NEXT record in the loop
                                v_prior_inventory_ending = v_temp_val
                                #
                                v_f13_value = str(v_temp_val)

                                # - F14, F15, F16 moved earlier in this script

                                # - F17
                                v_f17_name = "Net_Requirement"
                                #
                                # Can be greater-of-orders-or-forecast, plus (difference between greater-of-StartInv-and-zero and SafetyStock)
                                v_temp_val = float(v_f04_value)
                                #
                                # Check to see if the forecast is larger than the orders_completed... use forecast if this is true
                                if v_temp_val < float(v_f08_value):
                                    v_temp_val = float(v_f08_value)
                                #
                                # Subtract starting inventory
                                v_temp_val = v_temp_val - float(v_f10_value)
                                #
                                # If v_temp_val is less than zero, make it zero
                                if v_temp_val < float(0):
                                    v_temp_val = float(0)
                                #
                                # if v_temp_val is less than safety-stock, make it safety-stock
                                if v_temp_val < float(v_f14_value):
                                    v_temp_val = float(v_f14_value)
                                #
                                # WARNING: Yes, this is an incomplete/incorrect net-requirements calc.
                                #          But, it will be corrected in the rolling functions of COREDATA2
                                v_f17_value = str(v_temp_val)

                                # - F18
                                # - Determine an initial label value
                                # - Then make an effort to convert that to a corrective value
                                # - Then set a new and hopefully improved safety stock value.
                                # - parameter values: v_parm_dg_outcome_range, v_parm_dg_outcome_trigger, v_parm_dg_outcome_fix
                                    #
                                    # Example:
                                    #  DG_OUTCOME_RANGE   = [{"Field01": "VeryLow", "Field02": "Low", "Field03": "OK", "Field04": "High","Field05": "VeryHigh"}]
                                    #  DG_OUTCOME_TRIGGER = [{"Field01": ".50", "Field02": ".75", "Field03": "1.00", "Field04": "1.25","Field05": "1.50"}]
                                    #  DG_OUTCOME_FIX	  = [{"Field01": "1.50", "Field02": "1.25", "Field03": "1.00", "Field04": ".75", "Field05": ".50"}]

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

                                v_f18_name = "Outcome01"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = ""
                                # if (v_temp_rnd <= 40):
                                #     v_temp_val = "Worse"
                                # elif (v_temp_rnd <= 80):
                                #     v_temp_val = "Better"
                                # else:
                                #     v_temp_val = "Indeterminate"
                                v_f18_value = str(v_temp_val)

                                # - F19
                                v_f19_name = "Outcome02"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = ""
                                # if (v_temp_rnd <= 40):
                                #     v_temp_val = "Worse"
                                # elif (v_temp_rnd <= 80):
                                #     v_temp_val = "Better"
                                # else:
                                #     v_temp_val = "Indeterminate"
                                v_temp_val = ""
                                v_f19_value = str(v_temp_val)

                                # - F20
                                v_f20_name = "Outcome03"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = ""
                                # if (v_temp_rnd <= 40):
                                #     v_temp_val = "Worse"
                                # elif (v_temp_rnd <= 80):
                                #     v_temp_val = "Better"
                                # else:
                                #     v_temp_val = "Indeterminate"
                                v_f20_value = str(v_temp_val)

                                # - F21
                                v_f21_name = "Trend_type"
                                v_temp_rnd = random.randint(1, 100)
                                v_temp_val = v_trend_type_to_save_in_file
                                v_f21_value = str(v_temp_val)

                                # - F22
                                v_f22_name = "Trend_factor1"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_chance
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = v_current_trend_line_m
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_line_m
                                else:
                                    # Default to a line
                                    v_temp_val = v_current_trend_line_m
                                v_f22_value = str(v_temp_val)

                                # - F23
                                v_f23_name = "Trend_factor2"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_min
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = v_current_trend_line_b
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_line_b
                                else:
                                    # Default to a line
                                    v_temp_val = v_current_trend_line_b
                                v_f23_value = str(v_temp_val)

                                # - F24
                                v_f24_name = "Trend_factor3"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = v_current_trend_intermittent_max
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_phase
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_phase
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f24_value = str(v_temp_val)

                                # - F25
                                v_f25_name = "Trend_factor4"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_min
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_min
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f25_value = str(v_temp_val)

                                # - F26
                                v_f26_name = "Trend_factor5"
                                # Each trend_factor_x value changes depending on the trend for this combination
                                if (v_trend_type_to_save_in_file == "Intermittent01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Slope01"):
                                    v_temp_val = "n/a"
                                elif (v_trend_type_to_save_in_file == "Seasonal01"):
                                    v_temp_val = v_current_trend_seasonal_max
                                elif (v_trend_type_to_save_in_file == "Combined01"):
                                    v_temp_val = v_current_trend_seasonal_max
                                else:
                                    # Default to a line
                                    v_temp_val = "n/a"
                                v_f26_value = str(v_temp_val)

                                # - F27
                                v_f27_name = "Last_Period"
                                v_temp_val = v_current_date_element.strftime("%Y-%m-%d")
                                v_f27_value = str(v_temp_val)

                                # - F28
                                v_f28_name = "Last_X_Value"
                                v_temp_val = v_rowCounter_period
                                v_f28_value = str(v_temp_val)

                                # - F29
                                v_f29_name = "Last_Y_Value"
                                v_temp_val = v_current_calculated_volume_raw
                                v_f29_value = str(v_temp_val)


                                # -
                                # - Write the entire record to the target file
                                # -
                                v_current_output_row = '{ ' +   '"' + v_f01_name + '"' + ": " + '"' + v_f01_value + '"' \
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
                                                            + ', "' + v_f15_name + '"' + ": " + '"' + v_f15_value + '"' \
                                                            + ', "' + v_f16_name + '"' + ": " + '"' + v_f16_value + '"' \
                                                            + ', "' + v_f17_name + '"' + ": " + '"' + v_f17_value + '"' \
                                                            + ', "' + v_f18_name + '"' + ": " + '"' + v_f18_value + '"' \
                                                            + ', "' + v_f19_name + '"' + ": " + '"' + v_f19_value + '"' \
                                                            + ', "' + v_f20_name + '"' + ": " + '"' + v_f20_value + '"' \
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

                                # Update the number of records added to the output file
                                v_rowCounter_coredata += 1

                                # Convert the string to a JSON value
                                v_current_output_row_json = json.loads(v_current_output_row)

                                # Write out the result in CSV format
                                v_csv_file_coredata_writer.writerow(v_current_output_row_json.values())

                                if 1 == 2:
                                    print('-----')
                                    v_tempstr = str(v_rowCounter_matrix)
                                    print(v_tempstr.rjust(3,'0') + ", ", end = "")
                                    print(str(type(v_current_output_row)) + ", ", end = "")
                                    print(v_current_output_row)
                                    print(v_current_date_element.strftime("%Y-%m-%d"))


# ---
# - Show total number of MATRIX rows created
# ---
print("\n"*2)
print("Total new COREDATA rows created: " + str(v_rowCounter_coredata) )
print("\n"*2)


# ---
# - Close the file
# ---
# NOTE: auto-closed when using "with open..."


# ---
# - Display exit message
# ---
v_current_procedure_name = 'Generate ORDERS: INITIAL'
print("==================================================")
print("= " + v_current_procedure_name + ": END")
print("==================================================")
print("\n"*2)
sleep(1)


# ---
# - A bunch 'o newbies adding HTML to our AI/ML python code
# ---
print("</pre>")
print("<br>")
print("<br>")
print("</body>")
print("</html>")
