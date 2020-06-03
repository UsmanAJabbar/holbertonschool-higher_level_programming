#!/usr/bin/python3
"""LEAVING IT EMPTY"""


def load_from_json_file(filename):
    """
    ---------------------------
    METHOD: LOAD FROM JSON FILE
    ---------------------------
    Description:
        Deserializes a JSON file and returns a
        Python object from it
    Args:
        @filename: file containing JSON to
        deserialize
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as serializedjson:
        return json.load(serializedjson)
