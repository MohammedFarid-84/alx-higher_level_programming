#!/usr/bin/python3
from sys import argv


x = len(argv) - 1

if x == 1:
    y = ':'
elif x == 0:
    y = 's.'
else:
    y = 's:'

if __name__ == "__main__":
    print(f'{x} argument{y}')

    if x > 0:
        for n in range(1, len(argv)):
            print(f'{n}: {argv[n]}')
