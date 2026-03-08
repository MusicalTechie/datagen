
# ==================================================
# = File:	    DataGen_1220_Generate_locations_initial.py
# = Purpose:	Create initial list of LOCATIONS
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - 
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
v_current_procedure_name = 'Full Dataset: Generate LOCATIONS'



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



# Get LOC HIERARCHY
# v_parm_flag_loglevel = 1
if 1 == 1:
    v_list_loc_hier_names = json.loads(v_parm_dg_cust_hier_names)
    if int(v_parm_flag_loglevel) > 0:
        print('---')
        print('Parm   : ' + 'v_parm_dg_cust_hier_names')
        print('List   : ' + 'v_list_loc_hier_names')
        print('Type   : ' + str(type(v_list_loc_hier_names)))
        print('Count  : ' + str(len(v_list_loc_hier_names)))
        print('---')
    for v_parent_element in v_list_loc_hier_names:
        if int(v_parm_flag_loglevel) > 0:
            print(" - Parent row: " + str(v_parent_element))
        for v_child_element in v_parent_element:
            if int(v_parm_flag_loglevel) > 0:
                print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
    if int(v_parm_flag_loglevel) > 0:
        print('---')
        print("\n" * 2)

# Get LOCATIONS
# v_parm_flag_loglevel = 1
if 1 == 1:
    if int(v_parm_flag_loglevel) > 0:
        print('---')
        print("Parameter: v_parm_dg_customers \n<\n" + v_parm_dg_customers + "\n>")
        print('---')
    v_list_locs = json.loads(v_parm_dg_customers)
    if int(v_parm_flag_loglevel) > 0:
        print('Parm   : ' + 'v_parm_dg_customers')
        print('List   : ' + 'v_list_locs')
        print('Type   : ' + str(type(v_list_locs)))
        print('Count  : ' + str(len(v_list_locs)))
        print('---')
    for v_parent_element in v_list_locs:
        if int(v_parm_flag_loglevel) > 0:
            print(" - Parent row: " + str(v_parent_element))
        for v_child_element in v_parent_element:
            if int(v_parm_flag_loglevel) > 0:
                print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
    if int(v_parm_flag_loglevel) > 0:
        print('---')
        print("\n" * 2)




# ---
# - Generate initial list of LOCATIONS
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    #
    # Set variables
    # Use a preceding "r" to create a "raw" string without any accidental escaped characters like "backslash-b"
    #v_path_customers = r"C:\GitHub_Local_Repository\AIML\AppsAssoc_DEV_DataGen_002_Python-Faker\data_results\base\Master_CUSTOMERS.csv"
    v_path_customers        = v_parm_path_customers_base
    v_fileHandle_customers = ""
    v_rowCounter_customers = 0

    # open the CSV file
    # In Python 3 use the "newline" option within the "open" to prevent extra blank rows between actual data rows
    with open(v_path_customers, mode='w', newline='') as v_fileHandle_customers:

        # Create the csv object
        # Ensure that the csv writer will enclose all fields in double-quotes
        v_csv_file_object = csv.writer(v_fileHandle_customers, quoting=csv.QUOTE_ALL)

        # ---
        # - Write out the HEADER row
        # ---
        if 1 == 1:
            # Get LOCATION HIERARCHY
            # v_parm_flag_loglevel = 1
            if 1 == 1:
                v_list_loc_hier_names = json.loads(v_parm_dg_cust_hier_names)
                for v_parent_element in v_list_loc_hier_names:
                    v_csv_file_object.writerow(v_parent_element.values())
                    v_rowCounter_customers += 1

        # ---
        # - Write out CUSTOMER rows (for each row in the input, generate a random number of outputs)
        # ---
        # - WARNING: presumes the number of initial columns could vary so use relative positions
        # ---
        # -
        # - If there are FOUR hierarchy levels, then only compose the first THREE (v_parm_dg_cust_hier_lvls)
        # - as the last one will be generated (and can be skipped when reading the row).
        # -
        # - Then pick up the prefix, # digits, min #, max #
        # -
        # - Then generate a random number of objects to make between min and max
        # -
        # - Then loop through and generate them.
        # -
        # ---
        if 1 == 1:
            # ---
            v_current_obj_hier_limit = ""
            v_current_obj_hier_lvl = ""
            v_current_obj_prefix = ""
            v_current_obj_digits = 0
            v_current_obj_min = 0
            v_current_obj_max = 0
            # ---
            v_current_obj_rnd = 0
            # ---
            v_current_output_hier = ""
            v_current_output_item = ""
            v_current_output_row = ""
            # ---
            v_elementCounter_locations = 0
            v_rowCounter_customers = 0
            # ---
            v_list_locations = json.loads(v_parm_dg_customers)
            # ---
            for v_parent_element in v_list_locations:
                v_current_output_hier = ""
                v_current_output_item = ""
                v_current_output_row = ""
                v_elementCounter_locations = 0
                for v_child_element in v_parent_element:
                    v_elementCounter_locations += 1
                    #
                    # Compose the first part of the output row (the hierarchy); only if one-less than the total number of hierarchy levels
                    # SKIP the first element (a kind of row number used to help compose the CONFIG file rows)
                    if v_elementCounter_locations > 1:
                        if v_elementCounter_locations < (int(v_parm_dg_cust_hier_lvls) + 1):
                            v_current_output_hier = v_current_output_hier + ', "' + str(v_child_element) + '": "' + str(
                                v_parent_element[v_child_element]) + '"'
                    #
                    # Pick up the object PREFIX
                    if v_elementCounter_locations == (int(v_parm_dg_cust_hier_lvls) + 2):
                        v_current_obj_prefix = str(v_parent_element[v_child_element])
                    #
                    # Pick up the object # of DIGITS
                    if v_elementCounter_locations == (int(v_parm_dg_cust_hier_lvls) + 3):
                        v_current_obj_digits = int(v_parent_element[v_child_element])
                    #
                    # Pick up the object MIN
                    if v_elementCounter_locations == (int(v_parm_dg_cust_hier_lvls) + 4):
                        v_current_obj_min = int(v_parent_element[v_child_element])
                    #
                    # Pick up the object MAX
                    if v_elementCounter_locations == (int(v_parm_dg_cust_hier_lvls) + 5):
                        v_current_obj_max = int(v_parent_element[v_child_element])
                #
                # Pick a random number of objects to create
                # v_current_obj_rnd = int(random.randrange(v_current_obj_min, v_current_obj_max, 1))
                # v_current_obj_rnd = int(random.randrange(1, 5, 1))
                v_current_obj_rnd = random.randint(v_current_obj_min, v_current_obj_max)
                #
                # Trim off the first couple of characters from the hierarchy string which are a comma and a space from the config file
                v_current_output_hier = v_current_output_hier[2:]
                #
                # Loop based on random number and actually generate final object rows
                for v_object_index in range(1, v_current_obj_rnd+1):
                    # Add the composed item in the form of a JSON pair
                    v_object_index_str = str(v_object_index)
                    v_current_output_item = v_current_obj_prefix + v_object_index_str.rjust(v_current_obj_digits, '0')
                    # Put the hierarchy and the item together
                    v_current_output_row = '{' + v_current_output_hier + ', ' + '"LowestLevel": ' + '"' + v_current_output_item + '"' + '}'
                    #
                    # For each composed output row, write the result in CSV format to a file
                    # and increment the row count.
                    v_rowCounter_customers += 1
                    v_current_output_row_json = json.loads(v_current_output_row)
                    v_csv_file_object.writerow(v_current_output_row_json.values())
                    # print('-----')
                    # print("String type: " + str(type(v_current_output_row)))
                    # print("JSON type  : " + str(type(v_current_output_row_json)))
                    # print(str(v_rowCounter_customers))
                    # print(str(v_current_output_hier))
                    # print(str(v_current_output_item))
                    # print(str(v_current_output_row))
                    # print(str(v_current_output_row_json))
                    #print("Row: " + str(v_rowCounter_customers) + ", MIN: " + str(v_current_obj_min) + ", MAX: " + str(v_current_obj_max) + ", RND: " + str(v_current_obj_rnd))

# ---
# - Close the file
# ---
# NOTE: auto-closed when using "with open..."

# ---
# - Show total number of CUSTOMER rows created
# ---
print("\n"*2)
print("Total new CUSTOMER rows created: " + str(v_rowCounter_customers) )
print("\n"*2)

# ---
# - Display exit message
# ---
v_current_procedure_name = 'Generate LOCATION: INITIAL'
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

