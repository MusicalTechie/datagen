# ==================================================
# = File:        DataGen_1440_Acquire_ORGANIZATIONs_from_Oracle_via_REST.py
# = Purpose:     Execute a REST API call to acquire ORGANIZATION (supply network) information from a designated Oracle Cloud Fusion environment
# ==================================================
# = Notes, Warnings, Requirements:
# = ------------------------------------------------
# =  - Uses config: v_parm_fusion_*, v_parm_path_organizations_from_source.
# =  - Paginates via limit/offset until hasMore is false or totalItems is zero.
# =
# = Dates:
# = ------------------------------------------------
# =  - Created:     2026-MAR-11
# =  - Updated:
# ==================================================

import csv
import json
import logging
import os
import sys
from time import sleep

import requests
from requests.auth import HTTPBasicAuth

v_current_procedure_name = 'Acquire ORGANIZATIONs from Oracle via REST'

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": START")
logging.debug("==================================================")
logging.debug("\n" * 2)

from DataGen_1110_Load_config_main import *
sys.stdout.flush()
sys.stderr.flush()
logging.debug("\n" * 2)
sleep(1)

# --- REST API endpoint and request settings (defined in script) ---
v_api_rest_endpoint = "/fscmRestApi/resources/11.13.18.05/supplyNetworkOrganizations"
v_parm_fusion_url_base = (v_parm_fusion_url or "").rstrip("/")
v_api_rest_fullpath = v_parm_fusion_url_base + "/" + v_api_rest_endpoint.lstrip("/")
v_api_rest_api_headers = {"Content-Type": "application/json"}

v_api_rest_rec_limit = 500
v_api_rest_rec_offset = 0

v_api_rest_response_status_array = []
v_api_rest_response_response_array = []
v_api_rest_response_customers_array = []

v_response_limit = v_api_rest_rec_limit

# --- Acquire ORGANIZATIONs in blocks until no more records ---
while True:
    v_url_with_params = v_api_rest_fullpath + "?limit=" + str(v_response_limit) + "&offset=" + str(v_api_rest_rec_offset)
    logging.debug("Requesting: offset=" + str(v_api_rest_rec_offset) + ", limit=" + str(v_response_limit))

    try:
        v_resp = requests.get(
            v_url_with_params,
            headers=v_api_rest_api_headers,
            auth=HTTPBasicAuth(v_parm_fusion_username or "", v_parm_fusion_password or ""),
            timeout=120,
        )
    except Exception as e:
        logging.error("REST request failed: " + str(e))
        v_api_rest_response_status_array.append(-1)
        v_api_rest_response_response_array.append({"error": str(e)})
        break

    v_api_rest_response_status_array.append(v_resp.status_code)

    if v_resp.status_code != 200:
        logging.error("REST response status: " + str(v_resp.status_code) + " " + (v_resp.text or "")[:500])
        v_api_rest_response_response_array.append({"status_code": v_resp.status_code, "text": v_resp.text})
        break

    try:
        v_json = v_resp.json()
    except Exception as e:
        logging.error("REST response JSON parse failed: " + str(e))
        v_api_rest_response_response_array.append({"raw": v_resp.text[:1000]})
        break

    v_api_rest_response_response_array.append(v_json)

    v_has_more = v_json.get("hasMore", False)
    v_total_customers = v_json.get("totalResults", v_json.get("totalItems", -1))
    v_customers = v_json.get("items", [])

    for v_customer in v_customers:
        v_api_rest_response_customers_array.append(v_customer)

    if not v_has_more or (v_total_customers is not None and int(v_total_customers) == 0):
        logging.debug("No more records (hasMore=" + str(v_has_more) + ", totalItems/totalResults=" + str(v_total_customers) + ")")
        break

    if not v_customers:
        break

    v_api_rest_rec_offset += v_response_limit

    # Test line to force this loop to stop after one iteration
    if 1==2:
        if v_api_rest_response_status_array:
            logging.debug("Most recent REST response status: " + str(v_api_rest_response_status_array[-1]))
        if v_api_rest_response_response_array:
            logging.debug("Most recent REST response JSON: " + json.dumps(v_api_rest_response_response_array[-1], indent=2, default=str))
        break

# --- Write all organizations and attributes to quote-delimited CSV (overwrite if exists) ---
v_output_path = v_parm_path_organizations_from_source
v_output_dir = os.path.dirname(v_output_path)
if v_output_dir:
    os.makedirs(v_output_dir, exist_ok=True)

if v_api_rest_response_customers_array:
    v_keys_set = set()
    for v_customer in v_api_rest_response_customers_array:
        if isinstance(v_customer, dict):
            v_keys_set.update(v_customer.keys())
    v_all_keys = sorted(v_keys_set) if v_keys_set else (sorted(v_api_rest_response_customers_array[0].keys()) if v_api_rest_response_customers_array else [])

    with open(v_output_path, mode="w", newline="", encoding="utf-8") as v_f:
        v_writer = csv.writer(v_f, quoting=csv.QUOTE_ALL, delimiter=",")
        v_writer.writerow(v_all_keys)
        for v_customer in v_api_rest_response_customers_array:
            if isinstance(v_customer, dict):
                v_row = [v_customer.get(k, "") for k in v_all_keys]
                v_writer.writerow(v_row)
            else:
                v_writer.writerow([str(v_customer)])

    logging.debug("Wrote " + str(len(v_api_rest_response_customers_array)) + " organizations to " + str(v_output_path))
else:
    with open(v_output_path, mode="w", newline="", encoding="utf-8") as v_f:
        v_writer = csv.writer(v_f, quoting=csv.QUOTE_ALL, delimiter=",")
        v_writer.writerow([])
    logging.debug("No organizations to write; created empty file: " + str(v_output_path))

logging.debug("Total ORGANIZATION rows acquired via REST: " + str(len(v_api_rest_response_customers_array)))
logging.debug("\n" * 2)
logging.debug("==================================================")
logging.debug("= " + v_current_procedure_name + ": END")
logging.debug("==================================================")
logging.debug("\n" * 2)
sleep(1)
