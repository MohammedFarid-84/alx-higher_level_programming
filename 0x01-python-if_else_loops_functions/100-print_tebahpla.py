#!/usr/bin/python3


def print_alfa():
    x, y = 122, 89
    while x >= 98:
        print("{0:c}{1:c}".format(x,y), end='')
        x -= 2
        y -= 2

print_alfa()
