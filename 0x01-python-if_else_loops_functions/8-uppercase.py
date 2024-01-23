#!/usr/bin/python3


def uppercase(str):
    upr = list(range(ord('A'), ord('Z') + 1))
    lowr = list(range(ord('a'), ord('z') + 1))
    txupr = ""

    for i in str:
        try:
            indx = lowr.index(ord(i))
        except ValueError:
            indx = -1

        txupr += chr(upr[indx]) if indx != -1 else i

    print("{}".format(txupr))
