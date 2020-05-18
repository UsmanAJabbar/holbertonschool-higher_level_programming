#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        err = "Exception: Unknown format code 'd' for object of type "
        if isinstance(value, int):
            objtype = "'int'"
        elif isinstance(value, list):
            objtype = "'list'"
        elif isinstance(value, str):
            objtype = "'str'"
        elif isinstance(value, float):
            objtype = "'float'"
        print(err + objtype)
        return False
