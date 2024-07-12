#!/usr/bin/python3
import hidden_4 as libs


def printList(lst):
    for lib in lst:
        if not lib.startswith('__'):
            print(lib)


if __name__ == "__main__":
    myList = dir(libs)
    printList(myList)
