
# ==================================================
# = File:	    DataGen_1220_Generate_items_initial_ERR.py
# = Purpose:	Create initial list of ITEMS
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
v_current_procedure_name = 'Generate ORGANIZATIONS: INITIAL'

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
# Ensure 1210 output is visible when run via 1010 (flush immediately)
import sys
sys.stdout.flush()
sys.stderr.flush()
logging.debug("\n" * 2)
sleep(1)


# ---
# - Convert some variable content from JSON to LIST form
# ---
if 1 == 2:
    # Get ORGANIZATION HIERARCHY
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        v_list_organization_hier_names = json.loads(v_parm_dg_organization_hier_names)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug('Parm   : ' + 'v_parm_dg_organization_hier_names')
            logging.debug('List   : ' + str(v_list_organization_hier_names))
            logging.debug('Type   : ' + str(type(v_list_organization_hier_names)))
            logging.debug('Count  : ' + str(len(v_list_organization_hier_names)))
            logging.debug('---')
        for v_parent_element in v_list_organization_hier_names:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element))
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n" * 2)

    # Get ORGANIZATIONS
    # v_parm_flag_loglevel = 1
    if 1 == 1:
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("Parameter: v_parm_dg_organizations \n<\n" + v_parm_dg_organizations + "\n>")
            logging.debug('---')
        v_list_organizations = json.loads(v_parm_dg_organizations)
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('Parm   : ' + 'v_parm_dg_organizations')
            logging.debug('List   : ' + str(v_list_organizations))
            logging.debug('Type   : ' + str(type(v_list_organizations)))
            logging.debug('Count  : ' + str(len(v_list_organizations)))
            logging.debug('---')
        for v_parent_element in v_list_organizations:
            if int(v_parm_flag_loglevel) > 0:
                logging.debug(" - Parent row: " + str(v_parent_element))
            for v_child_element in v_parent_element:
                if int(v_parm_flag_loglevel) > 0:
                    logging.debug("   - " + v_child_element + ": [" + v_parent_element[v_child_element] + "]")
        if int(v_parm_flag_loglevel) > 0:
            logging.debug('---')
            logging.debug("\n" * 2)

    # instantiates the variable
    v_rowCounter_organizations=0

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


# ---
# - Generate initial list of ORGANIZATIONS (using shared hierarchy CSV generator)
# ---
from DataGen_shared_hierarchy_csv import generate_hierarchy_csv

if 1 == 2:
    v_path_organizations = v_parm_path_organizations_base
    logging.debug("Writing ORGANIZATIONS CSV to: " + str(v_path_organizations))
    v_rowCounter_organizations = generate_hierarchy_csv(
        v_parm_dg_organization_hier_names,
        v_parm_dg_organization_hier_lvls,
        v_parm_dg_organizations,
        v_path_organizations,
    )

# ---
# - Show total number of ORGANIZATION rows created
# ---
logging.debug("\n"*2)
logging.debug("Total new ORGANIZATION rows created: 0" )
# logging.debug("Total new ORGANIZATION rows created: " + str(v_rowCounter_organizations) )
logging.debug("\n"*2)


# ---
# - Display exit message
# ---
v_current_procedure_name = 'Generate ORGANIZATION: INITIAL'
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n"*2)
sleep(1)
