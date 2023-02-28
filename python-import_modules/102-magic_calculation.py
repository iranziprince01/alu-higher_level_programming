#!/usr/bin/python3


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        m = add(a, b)
        for j in range(4, 6):
            m = add(m, j)
        return (m)
    else:
        return (sub(a, b))
