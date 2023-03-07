#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix


def square_matrix_simple(matrix=[]):
    new = [[i ** 2 for i in j]for j in matrix]
    return new
