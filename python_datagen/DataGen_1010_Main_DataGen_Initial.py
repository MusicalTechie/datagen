
# ==================================================
# = File:	    DataGen_-1010-_Main_-_DataGen_Initial.py
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
# =  - Updated:     2022-JAN-13     Allan Barnard, config file loads, separate of parent and child code, basic data generation
# =  - Updated:     2022-FEB-24     Allan Barnard, adding weekly date buckets and extra fields to the COREDATA file
# =  - Updated:     2022-MAR-31     Allan Barnard, add more forecasting options (intermittent, seasonal, combined)
# =  - Updated:     2023-JUL-27     Allan Barnard, new directory, re-test, update old code, reload required libraries
# =  - Updated:     2023-OCT-10     Allan Barnard, execute in Dropbox under Anaconda environment
# =  - Updated:     2026-FEB-20     Allan Barnard, adjust for Oracle Fusion Cloud "Vision" instance
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
# -
# -     python -m pip install --upgrade pip
# -     pip install pandas
# -     pip install openpyxl
# -     pip install xlrd
# -
# ---
import configparser
import logging
import os
from time import sleep
import json

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'DataGenPY'

# ---
# - Ensure logging goes to terminal (and to log file once config is loaded via 1110)
# ---
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

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


logging.debug("The platform is: " + str(os.name))

# ---
# - Display a simple greeting
# ---
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n"*2)


# ---
# - Start in the correct directory
# - Resolve project root from this script's location (portable; no hardcoded user path)
# ---
v_script_dir = os.path.dirname(os.path.abspath(__file__))
v_appDir = os.path.dirname(v_script_dir)

v_cwd = os.getcwd()
logging.debug("... initial working directory: [" + v_cwd + "]")
os.chdir(v_appDir)
v_cwd = os.getcwd()
logging.debug("... application working directory: [" + v_cwd + "]")
logging.debug("\n"*2)


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

# try:
#     x_temp = v_parm_path_items_base
# except NameError:
#     x_temp = None  # or some default value

from DataGen_1110_Load_config_main import *
logging.debug("\n"*2)

# x_temp = v_parm_path_items_base


# ---
# - Convert some variable content from JSON to LIST form
# ---
if 1 == 1:
    # Get ITEM HIERARCHY
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        v_list_item_hier_names = json.loads(v_parm_dg_item_hier_names)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug('Parm   : ' + 'v_parm_dg_item_hier_names' )
            logging.debug('List   : ' + str(v_list_item_hier_names) )
            logging.debug('Type   : ' + str(type(v_list_item_hier_names)))
            logging.debug('Count  : ' + str( len(v_list_item_hier_names) ) )
            logging.debug('---')
        for v_parent_element in v_list_item_hier_names:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n"*2)

    # Get ITEMS
    v_parm_flag_loglevel = 1
    if 1 == 2:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("Parameter: v_parm_dg_items \n<\n" + v_parm_dg_items + "\n>")
            logging.debug('---')
        v_list_items = json.loads(v_parm_dg_items)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('Parm   : ' + 'v_parm_dg_items' )
            logging.debug('List   : ' + str(v_list_items) )
            logging.debug('Type   : ' + str(type(v_list_items)))
            logging.debug('Count  : ' + str( len(v_list_items) ) )
            logging.debug('---')
        for v_parent_element in v_list_items:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n"*2)

    # Get LOC HIERARCHY
    v_parm_flag_loglevel = 0
    if 1 == 1:
        v_list_loc_hier_names = json.loads(v_parm_dg_cust_hier_names)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug('Parm   : ' + 'v_parm_dg_cust_hier_names' )
            logging.debug('List   : ' + str(v_list_loc_hier_names) )
            logging.debug('Type   : ' + str(type(v_list_loc_hier_names)))
            logging.debug('Count  : ' + str( len(v_list_loc_hier_names) ) )
            logging.debug('---')
        for v_parent_element in v_list_loc_hier_names:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n"*2)

    # Get CUSTOMERS
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("Parameter: v_parm_dg_customers \n<\n" + v_parm_dg_customers + "\n>")
            logging.debug('---')
        v_list_locs = json.loads(v_parm_dg_customers)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('Parm   : ' + 'v_parm_dg_customers' )
            logging.debug('List   : ' + str(v_list_locs) )
            logging.debug('Type   : ' + str(type(v_list_locs)))
            logging.debug('Count  : ' + str( len(v_list_locs) ) )
            logging.debug('---')
        for v_parent_element in v_list_locs:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n"*2)


    # Get TRENDS
    #v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("Parameter: v_parm_dg_dmd_trends \n<\n" + v_parm_dg_dmd_trends + "\n>")
            logging.debug('---')
        v_list_dmd_trends = json.loads(v_parm_dg_dmd_trends)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('Parm   : ' + 'v_parm_dg_dmd_trends' )
            logging.debug('List   : ' + str(v_list_dmd_trends) )
            logging.debug('Type   : ' + str(type(v_list_dmd_trends)))
            logging.debug('Count  : ' + str( len(v_list_dmd_trends) ) )
            logging.debug('---')
        for v_parent_element in v_list_dmd_trends:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element) )
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n"*2)


# ---
# - Create INITIAL set of ORGANIZATIONS.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# - Only generate file if the app is set to use a random source.
# ---
if 1 == 1 and v_parm_app_source_type.lower() == "random":
    import sys
    sys.stdout.flush()
    sys.stderr.flush()
    from DataGen_1210_Generate_organizations_initial import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Create INITIAL set of ITEMS.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# - Only generate file if the app is set to use a random source.
# ---
if 1 == 1 and v_parm_app_source_type.lower() == "random":
    import sys
    sys.stdout.flush()
    sys.stderr.flush()
    from DataGen_1220_Generate_items_initial import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Create INITIAL set of CUSTOMERS.
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# - REQUIRED before 1230 (MATRIX) which reads CUSTOMERS_base.csv
# - Only generate file if the app is set to use a random source.
# ---
if 1 == 1 and v_parm_app_source_type.lower() == "random":
    import sys
    sys.stdout.flush()
    sys.stderr.flush()
    from DataGen_1230_Generate_customers_initial import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Create INITIAL set of MATRIX combinations (ITEM-to-CUSTOMER).
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1240_Generate_matrix_initial import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Create INITIAL set of CORE DATA (orders, forecast, etc)
# -
# - NOTE: using "from" and "import *" ensures that the variables are included
# -       into the scope of this calling script
# ---
if 1 == 1:
    from DataGen_1250_Generate_coredata_initial import *
    logging.debug("\n"*2)
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
    from DataGen_1260_PostProcess_coredata import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Create FBDI files
# ---
# - Reformat the COREDATA2 content into various FBDI files for loading into a Fusion environment.
# ---
if 1 == 1:
    from DataGen_1290_Compose_FBDI_Booking_History import *
    logging.debug("\n"*2)
    sleep(1)


# ---
# - Display exit message
# ---
v_current_procedure_name = 'DataGenPY'
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n"*2)
sleep(1)

