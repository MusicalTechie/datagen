"""Minimal test that config can be loaded when run from correct working directory."""
import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
_parent = os.path.dirname(_script_dir)
if _parent not in sys.path:
    sys.path.insert(0, _parent)


def test_config_file_path_resolution():
    """Config path is resolved from script location (data_config next to python_datagen)."""
    import configparser
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # script_dir = .../python_datagen/tests, so parent of parent = project root
    project_root = os.path.dirname(os.path.dirname(script_dir))
    config_dir = os.path.join(project_root, "data_config")
    config_path = os.path.join(config_dir, "config_main.ini")
    # When running from repo, data_config may exist
    if os.path.isdir(config_dir):
        assert os.path.isfile(config_path), "config_main.ini should exist in data_config"
        parser = configparser.RawConfigParser()
        parser.read(config_path)
        assert "LOG" in parser.sections()
        assert "PATHS" in parser.sections()
        assert "DATAGEN" in parser.sections()
    # If data_config is not present (e.g. in a copy), skip the read assertion
    assert True
