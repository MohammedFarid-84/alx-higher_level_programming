#!/usr/bin/pyhton3

def only_diff_elements(set_1, set_2):
    lst = set()
    for x in set_1:
        if x not in set_2 and x not in lst:
            lst.add(x)

    for x in set_2:
        if x not in set_1 and x not in lst:
            lst.add(x)

    return lst
