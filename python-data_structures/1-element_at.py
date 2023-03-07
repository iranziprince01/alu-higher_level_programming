#!/usr/bin/python3
# a function that retrieves an element from a list like in C

def element_at(my_list, idx):
    if idx < 0:
        return (None)

    if idx < len(my_list):
        return (my_list[idx])

    return (None)
