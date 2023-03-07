#!/usr/bin/python3
# 
def no_c(my_string):
    remove = ""
    for j in my_string:
        if j != 'c' and j != 'C':
            remove += j
    return (remove)
