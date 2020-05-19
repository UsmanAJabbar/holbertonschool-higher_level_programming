#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = (fct(*args))
        return result
    except Exception as failederr:
        from sys import stderr
        result = None
        stderr.write("Exception: {}\n".format(failederr))
        return result
