#!/usr/bin/python3
# Function that dislpays maximum integer of a list


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxNum = my_list[0]
    for j in my_list:
        if j > maxNum:
            maxNum = j
    return (maxNum)
