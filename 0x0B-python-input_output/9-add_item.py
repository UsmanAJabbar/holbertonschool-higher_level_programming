#!/usr/bin/python3
"""
----------------
SCRIPT: ADD ITEM
----------------
Description:
    Takes input from stdin and appends it
    onto a JSON list
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
    my_list = list(my_list)
except Exception:
    my_list = []
    save_to_json_file(my_list, "add_item.json")

my_list += argv[1:]

save_to_json_file(my_list, 'add_item.json')
