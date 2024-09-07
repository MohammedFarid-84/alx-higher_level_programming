#!/usr/bin/python3

def uniq_add(my_list=[]):
    lst = []
    resulte = 0
    for x in my_list:
        if x not in lst:
            lst.append(x)
    
    for x in lst:
        resulte += x

    return resulte
