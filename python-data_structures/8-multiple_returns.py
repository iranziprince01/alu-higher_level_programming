#!/usr/bin/python3
# a function that returns a tuple with the length of a
# +string and its first character.


def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        first = sentence[0]
    else:
        first = None
    return (lenght, first)
