#!/usr/bin/pyhton3

def common_elements(set_1, set_2):
    lst = set()
    for x in set_1:
        if x in set_2 and x not in lst:
            lst.add(x)
    return lst
