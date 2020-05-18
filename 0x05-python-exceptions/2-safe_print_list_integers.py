#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    dem_legit_values = 0

    for elements in range(x):
        try:
            print("{:d}".format(my_list[elements]), end='')
            dem_legit_values += 1
        except (ValueError, TypeError):
            continue
    print()
    return dem_legit_values
