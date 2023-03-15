#!/usr/bin/python3
"""
New class Square
"""


class Square:
    """ Defines a Square """
    def __init__(sep, c=0):
        if type(c) != int:
            raise TypeError("size must be an integer")
        if c < 0:
            raise ValueError("size must be >= 0")
        sep.__c = c
