#!/usr/bin/python3


def print_last_digit(number):
    rno = number % 10

    if number < 0:
        rno += 10 if rno < 0 else -10

    print(abs(rno), end='')
    return abs(rno)
