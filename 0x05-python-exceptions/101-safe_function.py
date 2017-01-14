#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
    except Exception as err:
        r = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return r
