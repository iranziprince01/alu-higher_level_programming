#!/usr/bin/python3

# import functions from calculation file
from calculator_1 import add, subtract, multiply, divide

if __name__ == '__main__':
    # define variables a and b
a = 10
b = 5

# perform the calculations
sum_ab = a + b
diff_ab = subtract(a, b)
prod_ab = a * b
quot_ab = a / b

# print the results
print("{} + {} = {}".format(a, b, sum_ab))
print("{} - {} = {}".format(a, b, diff_ab))
print("{} * {} = {}".format(a, b, prod_ab))
print("{} / {} = {}".format(a, b, quot_ab))