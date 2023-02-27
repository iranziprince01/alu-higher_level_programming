#!/usr/bin/python3
# python program to display calculating operations

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

# display the results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
