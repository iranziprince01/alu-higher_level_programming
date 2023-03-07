#!/usr/bin/python3
# a function that removes all characters c and C from a string


def no_c(my_string):
    remove = ""
    for j in my_string:
        if j != 'c' and j != 'C':
            remove += j
    return (remove)
