"""Tests for DataGen_shared_hierarchy_csv.generate_hierarchy_csv."""
import json
import os
import sys
import tempfile

# Ensure python_datagen is on path when running from project root or from python_datagen
_script_dir = os.path.dirname(os.path.abspath(__file__))
_parent = os.path.dirname(_script_dir)
if _parent not in sys.path:
    sys.path.insert(0, _parent)

from DataGen_shared_hierarchy_csv import generate_hierarchy_csv


def test_generate_hierarchy_csv_creates_file_and_returns_count():
    """Generate a tiny CSV and check file exists and row count is positive."""
    hier_names = [{"L1": "Region", "L2": "LowestLevel"}]
    # For hier_lvls=2: 1st key skipped, keys 2-3 = hierarchy, 4=prefix, 5=digits, 6=min, 7=max
    list_data = [
        {"Row": "1", "L1": "AMER", "L2": "X", "Prefix": "A", "Digits": "2", "Min": "1", "Max": "2"}
    ]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        path = f.name
    try:
        count = generate_hierarchy_csv(
            json.dumps(hier_names),
            "2",
            json.dumps(list_data),
            path,
        )
        assert count >= 1
        with open(path, "r") as f:
            lines = f.readlines()
        assert len(lines) >= 1
    finally:
        if os.path.exists(path):
            os.unlink(path)


def test_generate_hierarchy_csv_row_count_includes_header_and_data():
    """Row count should include header row(s) plus generated data rows."""
    hier_names = [{"L1": "X", "L2": "LowestLevel"}]
    list_data = [
        {"R": "1", "L1": "Y", "L2": "Z", "Prefix": "P", "Digits": "1", "Min": "2", "Max": "2"}
    ]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        path = f.name
    try:
        count = generate_hierarchy_csv(
            json.dumps(hier_names),
            "2",
            json.dumps(list_data),
            path,
        )
        # 1 header row + 2 data rows (Min=2, Max=2 -> 2 items)
        assert count == 1 + 2
    finally:
        if os.path.exists(path):
            os.unlink(path)
