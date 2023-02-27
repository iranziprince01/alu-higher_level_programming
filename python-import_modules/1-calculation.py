#!/usr/bin/python3

# import functions from calculation file
from calculator_1 import add, subtract, multiply, divide

# define variables a and b
a = 10
b = 5

# perform some math operations
sum_ab = add(a, b)
diff_ab = subtract(a, b)
prod_ab = multiply(a, b)
quot_ab = divide(a, b)

# display the results
print(f"The sum of {a} and {b} is {sum_ab}.")
print(f"The difference between {a} and {b} is {diff_ab}.")
print(f"The product of {a} and {b} is {prod_ab}.")
print(f"The quotient of {a} and {b} is {quot_ab}.")
