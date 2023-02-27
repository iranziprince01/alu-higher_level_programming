#!/usr/bin/python3

# import the add function from the give n file
from add_0 import add

if __name__ == '__main__':
    # define variables a and b
    a = 1
    b = 2

    # call the add function with arguments a and b and store the result in a variable called result
    result = add(a, b)

    # print the result using string formatting
    print("{} + {} = {}".format(a, b, result))

