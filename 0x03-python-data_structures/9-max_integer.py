#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        for i, elm in enumerate(my_list):
            big = elm if i == 0 else big
            if elm > big:
                big = elm
    else:
        big = None
    return big
