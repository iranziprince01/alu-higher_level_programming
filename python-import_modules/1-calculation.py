#!/usr/bin/python3
# import functions from calculation file

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

sum_result = add(a, b)
difference_result = subtract(a, b)
product_result = multiply(a, b)
quotient_result = divide(a, b)

print(f"The sum of {a} and {b} is {sum_result}.")
print(f"The difference between {a} and {b} is {difference_result}.")
print(f"The product of {a} and {b} is {product_result}.")
print(f"The quotient of {a} and {b} is {quotient_result}.")
