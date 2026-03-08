
# ==================================================
# = File:	    DataGen_1110_Load_config_main.py
# = Purpose:	Load primary application parameters
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
# =  - Created:     2021-DEC-21     Allan Barnard
# =  - Updated:     2022-APR-04     Allan Barnard, add COREDATA2 path options
# =  - Updated:     2022-AUG-08     Allan / Colin, add HTML output    
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


# ---
# - Define this procedure's name
# ---
v_current_procedure_name = 'Full Dataset: Configuration Values'


# ---
# - Adding HTML to our AI/ML python code
# ---
# print("Content-type: text/html\n")
# print("<html>")
# print("<title>" + v_current_procedure_name + "</title>")
# print("<body bgcolor=#B5CDE1>")
# print("<br>")
# print("<table border=1 cellspacing=0 cellpadding=8 width=432>")
# print(" <tr>")
# print("  <td align=center bgcolor=white>")
# print("	<b><font size=3>" + v_current_procedure_name + "</font></b>")
# print("  </td>")
# print(" </tr>")
# print("</table>")
# print("<br>")
# print("<br>")
# print("<pre>")


# print("The platform is: ", os.name)
# # print("big output\n" * 5)
# # wait for 5 seconds to clear screen
# # sleep(3)
# # screen_clear()
# # sleep(3)


# ---
# - Display a simple greeting
# ---
# print("\n", 10)
print("==================================================")
print("= " + v_current_procedure_name + ": START")
print("==================================================")
print("\n"*2)


# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("... current working directory: {0}".format(cwd))
print("\n")

# ---
# - Define location of config file
# ---
v_configParser = configparser.RawConfigParser()
v_configFileDir = 'C:\Apache\Apache24\cgi-bin\DataGen'
v_configFilePath = 'C:\Apache\Apache24\cgi-bin\DataGen\data_config\config_main.ini'

#v_configFileDir = '..\python_datagen\data_config'
#v_configFilePath = '..\data_config\config_main.ini'

v_config = configparser.ConfigParser(allow_no_value=True)
print ("... config file: ", v_configFilePath)
#sleep(1)

# TESTLINE: show content of directory
v_configDirContent = os.listdir(v_configFileDir)
print ("... directory files: ", v_configDirContent)

# ---
# - Read the config file
# ---
print("... reading config file")
v_configParser.read(v_configFilePath)
#sleep(1)

# Get groups/sections in the config file
print("... reading sections within config file")
v_configParser.sections()
print ("... section list: ", v_configParser.sections())
#sleep(1)

# ---
# - Pick up parameters from the config file group: LOG
# ---
print("")
v_parm_group = "LOG"
print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "FLAG_LOGLEVEL"
v_parm_flag_loglevel = v_configParser[v_parm_group][v_parm_current]
print("    - " + v_parm_current + " [" + v_parm_flag_loglevel + "]")
sleep(1)

# ---
# - Optional force-setting of flag that allows echo-back of variable content (log messages)
# ---
# v_parm_flag_loglevel = 0
# v_parm_flag_loglevel = 1


# ---
# - Pick up parameters from the config file group: APP
# ---
print("")
v_parm_group = "APP"
if int(v_parm_flag_loglevel) > 0:
    print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "APP_NAME"
v_parm_app_name = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_app_name + "]")
# ---
v_parm_current = "APP_VERSION"
v_parm_app_version = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_app_version + "]")
# ---
v_parm_current = "APP_ENVIRONMENT"
v_parm_app_environment = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_app_environment + "]")
# ---
v_parm_current = "APP_DEBUG"
v_parm_app_debug = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_app_debug + "]")
# ---
#sleep(1)


# ---
# - Pick up parameters from the config file group: PATHS
# ---
print("")
v_parm_group = "PATHS"
if int(v_parm_flag_loglevel) > 0:
    print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "PATH_DRIVE"
v_parm_path_drive = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_path_drive + "]")
# ---
v_parm_current = "PATH_TOP"
v_parm_path_top = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_top + "]")
# ---
v_parm_current = "PATH_MAIN"
v_parm_path_main = v_parm_path_drive + v_parm_path_top + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_main + "]")
# ---
v_parm_current = "PATH_CONFIG"
v_parm_path_config = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_PARAMETERS"
v_parm_path_parameters = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_CALENDAR"
v_parm_path_calendar = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_ITEMS_BASE"
v_parm_path_items_base = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_ITEMS_DELTA"
v_parm_path_items_delta = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_ITEMS_MERGED"
v_parm_path_items_merged = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_CUSTOMERS_BASE"
v_parm_path_customers_base = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_CUSTOMERS_DELTA"
v_parm_path_customers_delta = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_CUSTOMERS_MERGED"
v_parm_path_customers_merged = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_MATRIX_BASE"
v_parm_path_matrix_base = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_MATRIX_DELTA"
v_parm_path_matrix_delta = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_MATRIX_MERGED"
v_parm_path_matrix_merged = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA_BASE"
v_parm_path_coredata_base = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA_DELTA"
v_parm_path_coredata_delta = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA_MERGED"
v_parm_path_coredata_merged = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA2_BASE"
v_parm_path_coredata2_base = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA2_DELTA"
v_parm_path_coredata2_delta = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---
v_parm_current = "PATH_COREDATA2_MERGED"
v_parm_path_coredata2_merged = v_parm_path_main + v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_path_config + "]")
# ---

#sleep(1)


# ---
# - Pick up parameters from the config file group: DATABASE
# ---
print("")
v_parm_group = "DATABASE"
if int(v_parm_flag_loglevel) > 0:
    print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "DB_TYPE"
v_parm_db_ = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_db_ + "]")
# ---
v_parm_current = "DB_NAME"
v_parm_db_name = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_name + "]")
# ---
v_parm_current = "DB_USERNAME"
v_parm_db_username = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_username + "]")
# ---
v_parm_current = "DB_PASSWORD"
v_parm_db_password = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_password + "]")
# ---
v_parm_current = "DB_WALLET"
v_parm_db_wallet = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_wallet + "]")
# ---
v_parm_current = "DB_HOST"
v_parm_db_host = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_host + "]")
# ---
v_parm_current = "DB_PORT"
v_parm_db_port = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_db_port + "]")
# ---
#sleep(1)


# ---
# - Pick up parameters from the config file group: COMPANY
# ---
print("")
v_parm_group = "COMPANY"
if int(v_parm_flag_loglevel) > 0:
    print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "CO_NAME"
v_parm_co_name = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_co_name + "]")
# ---
v_parm_current = "CO_ADDR1"
v_parm_co_addr1 = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_addr1 + "]")
# ---
v_parm_current = "CO_ADDR2"
v_parm_co_addr2 = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_addr2 + "]")
# ---
v_parm_current = "CO_CITY"
v_parm_co_city = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_city + "]")
# ---
v_parm_current = "CO_REGION"
v_parm_co_region = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_region + "]")
# ---
v_parm_current = "CO_COUNTRY"
v_parm_co_country = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_country + "]")
# ---
v_parm_current = "CO_MAILCODE"
v_parm_co_mailcode = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_mailcode + "]")
# ---
v_parm_current = "CO_EMAIL"
v_parm_co_email = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_co_email + "]")
# ---
#sleep(1)


# ---
# - Pick up parameters from the config file group: DATAGEN
# ---
print("")
v_parm_group = "DATAGEN"
if int(v_parm_flag_loglevel) > 0:
    print("... loading parameters from group [" + v_parm_group + "]")
# ---
v_parm_current = "DG_CALENDAR_TYPE"
v_parm_dg_calendar_type = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_calendar_type + "]")
# ---
v_parm_current = "DG_PERIOD_TYPE"
v_parm_dg_period_type = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_period_type + "]")
# ---
v_parm_current = "DG_PERIOD_START"
v_parm_dg_period_start = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_period_start + "]")
# ---
v_parm_current = "DG_PERIOD_START_DOW"
v_parm_dg_period_start_dow = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_period_start_dow + "]")
# ---
v_parm_current = "DG_PERIOD_DIRECTION"
v_parm_dg_period_direction = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_period_direction + "]")
# ---
v_parm_current = "DG_DATE_HISTORY_START"
v_parm_dg_date_history_start = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_history_start + "]")
# ---
v_parm_current = "DG_DATE_HISTORY_END"
v_parm_dg_date_history_end = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_history_end + "]")
# ---
v_parm_current = "DG_DATE_PRESENT"
v_parm_dg_date_present = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_present + "]")
# ---
v_parm_current = "DG_DATE_OPENORDERS_START"
v_parm_dg_date_openorders_start = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_openorders_start + "]")
# ---
v_parm_current = "DG_DATE_OPENORDERS_END"
v_parm_dg_date_openorders_end = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_openorders_end + "]")
# ---
v_parm_current = "DG_DATE_FUTURE_START"
v_parm_dg_date_future_start = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_future_start + "]")
# ---
v_parm_current = "DG_DATE_FUTURE_END"
v_parm_dg_date_future_end = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_date_future_end + "]")
# ---
v_parm_current = "DG_ITEM_HIER_LVLS"
v_parm_dg_item_hier_lvls = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
        print("    - " + v_parm_current + " [" + v_parm_dg_item_hier_lvls + "]")
# ---
v_parm_current = "DG_ITEM_HIER_NAMES"
v_parm_dg_item_hier_names = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_item_hier_names + "]")
# ---
v_parm_current = "DG_ITEMS"
v_parm_dg_items = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_items + "]")
# ---
v_parm_current = "DG_LOC_HIER_LVLS"
v_parm_dg_cust_hier_lvls = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_cust_hier_lvls + "]")
# ---
v_parm_current = "DG_LOC_HIER_NAMES"
v_parm_dg_cust_hier_names = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_cust_hier_names + "]")
# ---
v_parm_current = "DG_MATRIX_NUM_COLS"
v_parm_dg_matrix_num_cols = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_matrix_num_cols + "]")
# ---
v_parm_current = "DG_MATRIX_COL_NAMES"
v_parm_dg_matrix_col_names = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_matrix_col_names + "]")
# ---
v_parm_current = "DG_COREDATA_NUM_COLS"
v_parm_dg_coredata_num_cols = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_coredata_num_cols + "]")
# ---
v_parm_current = "DG_COREDATA_COL_NAMES"
v_parm_dg_coredata_col_names = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_coredata_col_names + "]")
# ---
v_parm_current = "DG_LOCS"
v_parm_dg_customers = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_customers + "]")
# ---
v_parm_current = "DG_ATTACH_RATE"
v_parm_dg_attach_rate = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_attach_rate + "]")
# ---
v_parm_current = "DG_NUM_DMD_TRENDS"
v_parm_dg_num_dmd_trends = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_num_dmd_trends + "]")
# ---
v_parm_current = "DG_DMD_TRENDS"
v_parm_dg_dmd_trends = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_dmd_trends + "]")
# ---
v_parm_current = "DG_DMD_FC_VARIANCE"
v_parm_dg_dmd_fc_variance = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_dmd_fc_variance + "]")
# ---
v_parm_current = "DG_DMD_SS_FACTOR"
v_parm_dg_dmd_ss_factor = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_dmd_ss_factor + "]")
# ---
v_parm_current = "DG_PROD_CAPACITY_MIN"
v_parm_dg_prod_capacity_min = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_prod_capacity_min + "]")
# ---
v_parm_current = "DG_PROD_CAPACITY_MAX"
v_parm_dg_prod_capacity_max = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_prod_capacity_max + "]")
# ---
v_parm_current = "DG_PROD_CAPACITY_ROUND"
v_parm_dg_prod_capacity_round = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_prod_capacity_round + "]")
# ---
v_parm_current = "DG_OUTCOME_NUM_COLS"
v_parm_dg_outcome_num_cols = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_outcome_num_cols + "]")

# ---
v_parm_current = "DG_OUTCOME_RANGE"
v_parm_dg_outcome_range = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_outcome_range + "]")
# ---
v_parm_current = "DG_OUTCOME_TRIGGER"
v_parm_dg_outcome_trigger = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_outcome_trigger + "]")
# ---
v_parm_current = "DG_OUTCOME_FIX"
v_parm_dg_outcome_fix = v_configParser[v_parm_group][v_parm_current]
if int(v_parm_flag_loglevel) > 0:
    print("    - " + v_parm_current + " [" + v_parm_dg_outcome_fix + "]")
# ---
# #sleep(1)


# ---
# - Display exit message
# ---
print("==================================================")
print("= " + v_current_procedure_name + ": END")
print("==================================================")
print("\n"*2)
sleep(1)



# ---
# - A bunch 'o newbies adding HTML to our AI/ML python code
# ---
# print("</pre>")
# print("<br>")
# print("<br>")
# print("</body>")
# print("</html>")

