#!/usr/bin/python3
# a function that replaces an element in a list at a specific position


def new_in_list(my_list, idx, element):
    # Copy original list in other variable#
    m = my_list[:]
    if m is None:
        return
    if idx < 0 or idx > len(my_list) - 1:
        return (m)
    # Replace element#
    m[idx] = element
    return (m)
