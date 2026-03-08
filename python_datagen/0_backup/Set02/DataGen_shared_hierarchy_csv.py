# ==================================================
# = File:       DataGen_shared_hierarchy_csv.py
# = Purpose:    Shared logic to generate hierarchy-based CSV (items or customers)
# = Used by:    DataGen_1220_Generate_items_initial.py, DataGen_1230_Generate_customers_initial.py
# ==================================================

import csv
import json
import os
import random


def generate_hierarchy_csv(hier_names_json, hier_lvls, list_json, output_path):
    """
    Generate a CSV with header from hier_names and data rows from list_json.
    Each row in list_json defines a hierarchy prefix, digits, min, max; we generate
    a random count of codes (prefix + zero-padded index) and write one CSV row each.
    Returns total number of data rows written (excluding header rows).
    """
    hier_lvls_int = int(hier_lvls)
    hier_names_list = json.loads(hier_names_json) if isinstance(hier_names_json, str) else hier_names_json
    parent_list = json.loads(list_json) if isinstance(list_json, str) else list_json

    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    row_count = 0
    with open(output_path, mode='w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        # Header rows from hierarchy names
        for parent_element in hier_names_list:
            writer.writerow(parent_element.values())
            row_count += 1

        # Data rows: for each parent row, generate random number of child rows
        for parent_element in parent_list:
            output_hier = ""
            prefix = ""
            num_digits = 0
            min_val = 0
            max_val = 0
            element_counter = 0

            for child_key in parent_element:
                element_counter += 1
                if element_counter > 1 and element_counter < hier_lvls_int + 1:
                    output_hier = output_hier + ', "' + str(child_key) + '": "' + str(parent_element[child_key]) + '"'
                if element_counter == hier_lvls_int + 2:
                    prefix = str(parent_element[child_key])
                if element_counter == hier_lvls_int + 3:
                    num_digits = int(parent_element[child_key])
                if element_counter == hier_lvls_int + 4:
                    min_val = int(parent_element[child_key])
                if element_counter == hier_lvls_int + 5:
                    max_val = int(parent_element[child_key])

            n = random.randint(min_val, max_val)
            output_hier = output_hier[2:]  # drop leading ", "

            for idx in range(1, n + 1):
                code = prefix + str(idx).rjust(num_digits, '0')
                row_dict_str = '{' + output_hier + ', ' + '"LowestLevel": ' + '"' + code + '"' + '}'
                row_dict = json.loads(row_dict_str)
                writer.writerow(row_dict.values())
                row_count += 1

    return row_count
