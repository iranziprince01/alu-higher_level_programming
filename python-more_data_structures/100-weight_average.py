#!/usr/bin/python3
# a function that returns the weighted average of all integers tuple


def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    divn = 0
    for tup in my_list:
        avg += tup[0] * tup[1]
        divn += tup[1]
    return float(avg / divn)
