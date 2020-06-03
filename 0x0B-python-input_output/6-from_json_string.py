#!/usr/bin/python3
"""THE CHECKER'S SERIOUSLY MAKING ME DO THIS"""


def from_json_string(my_str):
    """
    ------------------------
    METHOD: FROM_JSON_STRING
    ------------------------
    Description:
        Returns a serialized repr of a python
        object
    Args:
        @my_str: string input
    """
    import json
    return json.loads(my_str)
