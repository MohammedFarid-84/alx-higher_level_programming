#!/usr/bin/python3

def uppercase(str):
    u = list(range(ord('A'), ord('Z') + 1))
    l = list(range(ord('a'), ord('z') + 1))
    txupr = ""

    for i  in str:
        try:
            indx = l.index(ord(i))
        except:
            indx = -1

        txupr += chr(u[indx]) if indx != -1 else i

    print("{}".format(txupr))
