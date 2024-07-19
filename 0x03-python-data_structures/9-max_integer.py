#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0
    if my_list:
        for elm in my_list:
            if elm > big:
                big = elm
    else:
        big = None
    return big
