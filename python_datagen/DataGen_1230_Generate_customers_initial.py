
# ==================================================
# = File:	    DataGen_1230_Generate_customers_initial.py
# = Purpose:	Create initial list of CUSTOMERS
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
# =  - Updated:     2023-OCT-10     Allan Barnard, execute in Dropbox under Anaconda environment
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
import random

# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Generate CUSTOMERS: INITIAL'

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


# Get LOC HIERARCHY
# v_parm_flag_loglevel = 1
if 1 == 1:
    v_list_loc_hier_names = json.loads(v_parm_dg_cust_hier_names)
    if int(v_parm_flag_loglevel) > 0:
        logging.debug('---')
        logging.debug('Parm   : ' + 'v_parm_dg_cust_hier_names')
        logging.debug('List   : ' + str(v_list_loc_hier_names))
        logging.debug('Type   : ' + str(type(v_list_loc_hier_names)))
        logging.debug('Count  : ' + str(len(v_list_loc_hier_names)))
        logging.debug('---')
    for v_parent_element in v_list_loc_hier_names:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug(" - Parent row: " + str(v_parent_element))
        for v_child_element in v_parent_element:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
    if int(v_parm_flag_loglevel) > 0:
        logging.debug('---')
        logging.debug("\n" * 2)


# Get CUSTOMERS
# v_parm_flag_loglevel = 1
if 1 == 1:
    if int(v_parm_flag_loglevel) > 0:
        logging.debug('---')
        logging.debug("Parameter: v_parm_dg_customers \n<\n" + v_parm_dg_customers + "\n>")
        logging.debug('---')
    v_list_locs = json.loads(v_parm_dg_customers)
    if int(v_parm_flag_loglevel) > 0:
        logging.debug('Parm   : ' + 'v_parm_dg_customers')
        logging.debug('List   : ' + str(v_list_locs))
        logging.debug('Type   : ' + str(type(v_list_locs)))
        logging.debug('Count  : ' + str(len(v_list_locs)))
        logging.debug('---')
    for v_parent_element in v_list_locs:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug(" - Parent row: " + str(v_parent_element))
        for v_child_element in v_parent_element:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
    if int(v_parm_flag_loglevel) > 0:
        logging.debug('---')
        logging.debug("\n" * 2)


# ---
# - Generate initial list of CUSTOMERS (using shared hierarchy CSV generator)
# ---
from DataGen_shared_hierarchy_csv import generate_hierarchy_csv

if 1 == 1:
    v_path_customers = v_parm_path_customers_base
    v_rowCounter_customers = generate_hierarchy_csv(
        v_parm_dg_cust_hier_names,
        v_parm_dg_cust_hier_lvls,
        v_parm_dg_customers,
        v_path_customers,
    )

# ---
# - Show total number of CUSTOMER rows created
# ---
logging.debug("\n"*2)
logging.debug("Total new CUSTOMER rows created: " + str(v_rowCounter_customers) )
logging.debug("\n"*2)

# ---
# - Display exit message
# ---
v_current_procedure_name = 'Generate CUSTOMER: INITIAL'
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n"*2)
sleep(1)
