#!/usr/bin/python3

for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            continue
        else:
            if i < 8 and j < 10:
                print("{0}{1}, ".format(i, j), end='')
            else:
                print("{0}{1}".format(i, j))
