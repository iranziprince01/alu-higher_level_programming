#!/usr/bin/python3
# a function that returns a key with the biggest integer value.


def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary, key=a_dictionary.get)
        return (max_value)
