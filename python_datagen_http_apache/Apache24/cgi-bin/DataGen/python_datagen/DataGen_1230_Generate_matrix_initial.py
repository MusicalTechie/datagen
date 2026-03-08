#!C:\Users\Administrator\AppData\Local\Programs\Python\Python310\python.exe

# ==================================================
# = File:	    DataGen_1230_Generate_matrix_initial.py
# = Purpose:	Create initial MATRIX where ITEMS are joined to some LOCATIONS
# =             (as if a sale of an ITEM were made at a particular LOCATION)
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
# -     - Select your current project.
# -    - Click the Python Interpreter tab within your project tab.
# -    - Click the small + symbol to add a new library to the project.
# -    - Now type in the library to be installed, for example Pandas, and click Install Package
# ---
import configparser
import os
from time import sleep
import json
import csv
import random


# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Full Dataset: Generate MATRIX'



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
# - Pick up the TRENDS
# ---
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


# ---
# - Create a MATRIX of ITEMs and LOCATIONs
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
    #v_path_customers = r"C:\GitHub_Local_Repository\AIML\AppsAssoc_DEV_DataGen_002_Python-Faker\data_results\base\Master_LOCATIONS.csv"
    # -
    v_path_items            = v_parm_path_items_base
    v_path_customers        = v_parm_path_customers_base
    v_path_matrix           = v_parm_path_matrix_base
    # -
    v_fileHandle_items      = ""
    v_fileHandle_customers  = ""
    v_fileHandle_matrix     = ""
    # -
    v_rowCounter_items      = 0
    v_rowCounter_customers  = 0
    v_rowCounter_matrix     = 0

    # ---
    # - Open MATRIX to WRITE the header (it'll close and re-open continually for appending later)
    # ---
    with open(v_path_matrix, mode='w', newline='') as v_fileHandle_matrix:

        # Create the csv write-object
        v_csv_file_matrix_writer = csv.writer(v_fileHandle_matrix, quoting=csv.QUOTE_ALL)
        v_rowCounter_matrix += 1
        v_current_output_row_json_list = json.loads(v_parm_dg_matrix_col_names)
        v_current_output_row_json_dict = json.loads(v_parm_dg_matrix_col_names)
        #
        # This is odd, but the first JSON.LOAD results in a "LIST" type of variable.
        # The output needs a "DICTIONARY" or true "JSON" type.
        # There are several ways to convert a LIST to a DICT.
        # Since there is only ONE ROW in this LIST, cheating and using a loop to convert to DICT type.
        for v_element in v_current_output_row_json_list:
            v_current_output_row_json_dict = v_element
        v_csv_file_matrix_writer.writerow( v_current_output_row_json_dict.values() )
        # print('-----')
        # print ( "Parameter type: " + str(type(v_parm_dg_matrix_col_names)))
        # print ( "JSON list type: " + str(type(v_current_output_row_json_list)))
        # print ( "JSON list len : " + str(len(v_current_output_row_json_list) ))
        # print ( "JSON dict type: " + str(type(v_current_output_row_json_dict)))
        # print(v_parm_dg_matrix_col_names)
        # print(v_current_output_row_json_list)
        # for v_element in v_current_output_row_json_list:
        #     print("Loop row type   : " + str(type(v_element)))
        #     print("Loop row content: " + str(v_element))


    # ---
    # - Open ITEMs for READ (but skip first header row)
    # ---
    with open(v_path_items, mode='r') as v_fileHandle_items:

        # Create the csv read-object
        v_csv_file_item_reader = csv.reader(v_fileHandle_items)

        # NOTE: these particular rows are "value only" and will read as "LIST" objects rather than "DICTIONARY" objects
        for v_row_item in v_csv_file_item_reader:
            v_rowCounter_items += 1
            v_tempstr = str(v_rowCounter_items)
            # print(v_tempstr.rjust(3,'0') + ", ", end = "")
            # print(str(type(v_row_item)) + ", ", end = "")
            # print(v_row_item)

            # Reset the LOCATION row-counter so that the header row can be detected every time the next ITEM is picked up
            v_rowCounter_customers = 0

            # ---
            # - Open LOCATIONs for READ (skip first row of ITEMs as it will be a header)
            # ---
            if v_rowCounter_items > 1:
                with open(v_path_customers, mode='r') as v_fileHandle_customers:

                    # Create the csv read-object
                    v_csv_file_customer_reader = csv.reader(v_fileHandle_customers)

                    # NOTE: these particular rows are "value only" and will read as "LIST" objects rather than "DICTIONARY" objects
                    for v_row_customer in v_csv_file_customer_reader:
                        v_rowCounter_customers += 1
                        v_tempstr = str(v_rowCounter_customers)
                        # print('     ' + v_tempstr.rjust(3, '0') + ", ", end="")
                        # print(str(type(v_row_item)) + ", ", end="")
                        # print(v_row_customer)

                        # ---
                        # - Open MATRIX for WRITE (skip first row of LOCATIONs as it will be a header)
                        # ---
                        if v_rowCounter_customers > 1:
                            #
                            # Only write a final MATRIX record if a random number is within the attach-rate percentage
                            v_temp_rnd   = random.randint(1,100)
                            if ( v_temp_rnd <= int(v_parm_dg_attach_rate) ):
                                #
                                with open(v_path_matrix, mode='a+', newline='') as v_fileHandle_matrix:
                                    #
                                    # Create the csv write-object
                                    v_csv_file_matrix_writer = csv.writer(v_fileHandle_matrix, quoting=csv.QUOTE_ALL)
                                    #
                                    # Update the counter
                                    v_rowCounter_matrix += 1
                                    #
                                    # Compose the matrix columns
                                    # -
                                    v_f01_name  = "Item"
                                    v_f01_value = v_row_item[-1]
                                    # -
                                    v_f02_name  = "Location"
                                    v_f02_value = v_row_customer[-1]
                                    # -
                                    v_f03_name  = "Status"
                                    v_temp_rnd  = random.randint(1,100)
                                    v_temp_val  = ""
                                    if (v_temp_rnd <= 25):
                                        v_temp_val = "Inactive"
                                    else:
                                        v_temp_val = "Active"
                                    v_f03_value = str( v_temp_val )
                                    # -
                                    v_f04_name  = "LifeCycle"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = ""
                                    if (v_temp_rnd <= 25):
                                        v_temp_val = "NPI"
                                    elif (v_temp_rnd <= 50):
                                        v_temp_val = "Core"
                                    else:
                                        v_temp_val = "EOL"
                                    v_f04_value = str( v_temp_val )
                                    # -
                                    v_f05_name  = "TrendNPI"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = ""
                                    if (v_temp_rnd <= 10):
                                        v_temp_val = "Intermitent"
                                    elif (v_temp_rnd <= 30):
                                        v_temp_val = "Slope01"
                                    elif (v_temp_rnd <= 50):
                                        v_temp_val = "Seasonal01"
                                    else:
                                        v_temp_val = "Combined01"
                                    v_f05_value = str( v_temp_val )
                                    # -
                                    v_f06_name  = "TrendCORE"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = ""
                                    if (v_temp_rnd <= 10):
                                        v_temp_val = "Intermitent"
                                    elif (v_temp_rnd <= 30):
                                        v_temp_val = "Slope01"
                                    elif (v_temp_rnd <= 50):
                                        v_temp_val = "Seasonal01"
                                    else:
                                        v_temp_val = "Combined01"
                                    v_f06_value = str( v_temp_val )
                                    # -
                                    v_f07_name  = "TrendEOL"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = ""
                                    if (v_temp_rnd <= 10):
                                        v_temp_val = "Intermitent"
                                    elif (v_temp_rnd <= 30):
                                        v_temp_val = "Slope01"
                                    elif (v_temp_rnd <= 50):
                                        v_temp_val = "Seasonal01"
                                    else:
                                        v_temp_val = "Combined01"
                                    v_f07_value = str( v_temp_val )
                                    # -
                                    v_f08_name  = "DateNPI"
                                    v_f08_value = "2018-01-01"
                                    # -
                                    v_f09_name  = "DateCORE"
                                    v_f09_value = "2019-01-01"
                                    # -
                                    v_f10_name  = "DateEOL"
                                    v_f10_value = "2025-01-01"
                                    # -
                                    v_f11_name  = "SafetyStockType"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = ""
                                    if (v_temp_rnd <= 33):
                                        v_temp_val = "Fixed"
                                    elif (v_temp_rnd <= 66):
                                        v_temp_val = "Periods"
                                    else:
                                        v_temp_val = "Forecast"

                                    # Temporarily set this to a fixed value of "Rolling_6-Period_Average"
                                    v_temp_val="Rolling_6-Period_Average"
                                    v_f11_value = str( v_temp_val )
                                    # -
                                    v_f12_name  = "InitialSafetyStockValue"
                                    v_temp_rnd = random.randint(1, 100)
                                    v_temp_val = str( v_temp_rnd )
                                    v_f12_value = str( v_temp_val )
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
                                                        + ' }'
                                    v_current_output_row_json = json.loads(v_current_output_row)
                                    v_csv_file_matrix_writer.writerow(v_current_output_row_json.values())
                                    # print('-----')
                                    # v_tempstr = str(v_rowCounter_matrix)
                                    # print(v_tempstr.rjust(3,'0') + ", ", end = "")
                                    # print(str(type(v_current_output_row)) + ", ", end = "")
                                    # print(v_current_output_row)

# ---
# - Show total number of MATRIX rows created
# ---
print("\n"*2)
print("ITEM-to-LOCATION attach-rate : " + str(v_parm_dg_attach_rate) + "%" )
print("Total new MATRIX rows created: " + str(v_rowCounter_matrix) )
print("\n"*2)


# ---
# - Close the file
# ---
# NOTE: auto-closed when using "with open..."


# ---
# - Display exit message
# ---
v_current_procedure_name = 'Generate MATRIX: INITIAL'
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

