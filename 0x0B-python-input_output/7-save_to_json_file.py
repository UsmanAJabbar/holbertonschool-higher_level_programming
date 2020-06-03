#!/usr/bin/python3
"""CHANGE.ORG/DOCSTRINGKILL REMOVE THIS DOCSTRING CHECK FROM THE CHECKER"""


def save_to_json_file(my_obj, filename):
    """
    -------------------------
    METHOD: SAVE TO JSON FILE
    -------------------------
    Description:
        Serializes given object into JSON format
        and dumps it into a json file.
    Args:
        @my_obj: object being imported from main
        @filename: filename to write dump to
    """
    import json
    with open(filename, mode='w', encoding="utf-8") as new_file:
        json.dump(my_obj, new_file)
