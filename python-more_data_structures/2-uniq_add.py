#!/usr/bin/python3
# a function that adds all unique integers in
# +a list (only once for each integer)


def uniq_add(my_list=[]):
    sum_i = sum(set(my_list))
    return (sum_i)
