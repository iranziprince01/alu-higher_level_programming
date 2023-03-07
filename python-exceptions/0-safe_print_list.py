#!/usr/bin/python3
# a function that prints x elements of a list.


def safe_print_list(my_list=[], x=0):
    k = 0  # Counter variable
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            k += 1

        except IndexError:
            break
    print()
    return (k)
