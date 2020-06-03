#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

from sys import argv
try:
    my_list = load_from_json_file("add_item.json")
    my_list = list(my_list)
except Exception:
    my_list = []
    save_to_json_file(my_list,"add_item.json")
    
for elements in range(1, len(argv)):
    my_list.append(argv[elements])

save_to_json_file(my_list, 'add_item.json')
