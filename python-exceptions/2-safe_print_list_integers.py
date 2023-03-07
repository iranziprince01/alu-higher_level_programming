#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    h = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            h += 1
        except (TypeError, ValueError):
            pass
    print()
    return (h)
