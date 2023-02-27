#!/usr/bin/python3

# import functions from calculation file
from calculator_1 import add, subtract, multiply, divide

if __name__ == '__main__':

# define variables a and b
a = 10
b = 5

# perform some math operations
sum_ab = add(a, b)
diff_ab = subtract(a, b)
prod_ab = multiply(a, b)
quot_ab = divide(a, b)

# display the results
print("The sum of {} and {} is: {}".format(a, b, sum_ab))
print("The difference between {} and {} is: {}".format(a, b,diff_ab))
print("The Product of {} and {} is: {}".format(a, b, prod_ab))
print("The qotient of {} and {} is: {}".format(a, b, quot_ab))
