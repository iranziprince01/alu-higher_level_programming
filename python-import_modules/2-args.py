#!/usr/bin/python3

# python program to display arguments of the word

if __name__ == '__main__':
    import sys

    count = len(sys.argv) - 1
    if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:\n")
    print("1: Hello")
else:
    print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i +1, sys.argv[i + 1]))

