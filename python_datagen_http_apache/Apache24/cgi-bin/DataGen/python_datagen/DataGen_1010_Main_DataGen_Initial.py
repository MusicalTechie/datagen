
# ==================================================
# = File:	    DataGen_1010_Main_DataGen_Initial.py
# = Purpose:	Launch initial DataGen app, read config file, and allow user to take action
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Will run one or more config-file loads to set up variables
# =  - Using the "import" method to execute external files (not call(["python", "your_file.py"]) )
# =  - 
# =  - 
# = 
# = Dates:
# = ------------------------------------------------
# =  - Created:     2021-DEC-21     Allan Barnard
# =  - Updated:     2022-JAN-13     Allan Barnard, config file loads, separate of parent and
# =                                                child code, basic data generation
# =  - Updated:     2022-FEB-24     Allan Barnard, adding weekly date buckets and extra fields to the COREDATA file
# =  - Updated:     2022-MAR-31     Allan Barnard, add more forecasting options (intermittent, seasonal, combined)
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
# -      - Select your current project.
# -    - Click the Python Interpreter tab within your project tab.
# -    - Click the small + symbol to add a new library to the project.
# -    - Now type in the library to be installed, for example Pandas, and click Install Package
# ---
import configparser

import os

from time import sleep

import json


# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'DataGenPY'

# ---
# - Clear the console window
# ---
# The screen clear function
def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text


print("The platform is: ", os.name)
# print("big output\n" * 5)
# wait for 5 seconds to clear screen
# sleep(3)
# screen_clear()
# sleep(3)


# ---
# - Display a simple greeting
# ---
print("==================================================")
print("= " + v_current_procedure_name + ": START")
print("==================================================")
print("\n"*2)


# ---
# - Start in the correct directory
# - Use a preceding "r" to create a "raw" string without any accidental escaped characters like "backslash-b"
# ---
v_appDir = r'C:\Apache\Apache24\cgi-bin\DataGen\data_config\python_datagen'

v_cwd = os.getcwd()
print("... initial working directory: [" + v_cwd + "]")
os.chdir(v_appDir)
print("... application working directory: [" + v_cwd + "]")
print("\n"*2)


# ----------
# ---
# - Call other Python files using "import"
# - WARNING: do NOT include ".py" at the end of the file name when using import
# -
# - An alternative would be: all(["python", "your_file.py"])
# ---
# ----------

# ---
# - Pick up primary application parameters
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
from DataGen_1110_Load_config_main import *
print("\n"*2)


# ---
# - Convert some variable content from JSON to LIST form
# ---
if 1 == 1:
    # Get ITEM HIERARCHY
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        v_list_item_hier_names = json.loads(v_parm_dg_item_hier_names)
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print('Parm   : ' + 'v_parm_dg_item_hier_names' )
            print('List   : ' + 'v_list_item_hier_names' )
            print('Type   : ' + str(type(v_list_item_hier_names)))
            print('Count  : ' + str( len(v_list_item_hier_names) ) )
            print('---')
        for v_parent_element in v_list_item_hier_names:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n"*2)

    # Get ITEMS
    v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_items \n<\n" + v_parm_dg_items + "\n>")
            print('---')
        v_list_items = json.loads(v_parm_dg_items)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_items' )
            print('List   : ' + 'v_list_items' )
            print('Type   : ' + str(type(v_list_items)))
            print('Count  : ' + str( len(v_list_items) ) )
            print('---')
        for v_parent_element in v_list_items:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n"*2)

    # Get LOC HIERARCHY
    v_parm_flag_loglevel = 0
    if 1 == 1:
        v_list_loc_hier_names = json.loads(v_parm_dg_cust_hier_names)
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print('Parm   : ' + 'v_parm_dg_cust_hier_names' )
            print('List   : ' + 'v_list_loc_hier_names' )
            print('Type   : ' + str(type(v_list_loc_hier_names)))
            print('Count  : ' + str( len(v_list_loc_hier_names) ) )
            print('---')
        for v_parent_element in v_list_loc_hier_names:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n"*2)

    # Get LOCATIONS
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_customers \n<\n" + v_parm_dg_customers + "\n>")
            print('---')
        v_list_locs = json.loads(v_parm_dg_customers)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_customers' )
            print('List   : ' + 'v_list_locs' )
            print('Type   : ' + str(type(v_list_locs)))
            print('Count  : ' + str( len(v_list_locs) ) )
            print('---')
        for v_parent_element in v_list_locs:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n"*2)


    # Get TRENDS
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("Parameter: v_parm_dg_dmd_trends \n<\n" + v_parm_dg_dmd_trends + "\n>")
            print('---')
        v_list_dmd_trends = json.loads(v_parm_dg_dmd_trends)
        if int(v_parm_flag_loglevel) > 0:
            print('Parm   : ' + 'v_parm_dg_dmd_trends' )
            print('List   : ' + 'v_list_dmd_trends' )
            print('Type   : ' + str(type(v_list_dmd_trends)))
            print('Count  : ' + str( len(v_list_dmd_trends) ) )
            print('---')
        for v_parent_element in v_list_dmd_trends:
            if int(v_parm_flag_loglevel) > 0:
                print(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    print("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            print('---')
            print("\n"*2)

# ---
# - Create INITIAL set of ITEMS.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1210_Generate_items_initial import *
    print("\n"*2)
    sleep(1)



# ---
# - Create INITIAL set of LOCATIONS.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1220_Generate_customers_initial import *
    print("\n"*2)
    sleep(1)



# ---
# - Create INITIAL set of MATRIX combinations (ITEM-to-LOCATION).
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1230_Generate_matrix_initial import *
    print("\n"*2)
    sleep(1)



# ---
# - Create INITIAL set of CORE DATA (orders, forecast, etc)
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1240_Generate_coredata_initial import *
    print("\n"*2)
    sleep(1)



# ---
# - WARNING: as of 2022-Mar-04 Myles, Satish, and the balding Canadian have added loops
# ---
# - Read the initial coredata file, post-process it for rolling averages and similar,
# - and then write the new version of the file out as a new name.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1250_PostProcess_coredata import *
    print("\n"*2)
    sleep(1)



# ---
# - Display exit message
# ---
v_current_procedure_name = 'DataGenPY'
print("==================================================")
print("= " + v_current_procedure_name + ": END")
print("==================================================")
print("\n"*2)
sleep(1)

