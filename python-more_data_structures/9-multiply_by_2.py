#!/usr/bin/python3
# a function that returns a new dictionary with all
# +values multiplied by 2


def multiply_by_2(a_dictionary):
    new = {}
    for j in a_dictionary:
        new[j] = a_dictionary[j] * 2
    return (new)
