#!/usr/bin/python3
# a function that replaces all occurrences of an element by
# +another in a new list


def search_replace(my_list, search, replace):
    new = [i if i != search else replace for i in my_list]
    return (new)
