#!/usr/bin/python3
# a function that prints an integer


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)

    return (True)
