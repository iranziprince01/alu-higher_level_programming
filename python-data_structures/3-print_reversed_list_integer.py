#!/usr/bin/python3
# a function that prints all integers of a list, in reverse order


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    reverse = reversed(my_list)
    for j in reverse:
        print("{:d}".format(j))
