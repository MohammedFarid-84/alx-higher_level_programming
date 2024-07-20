#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        for i, elm in enumerate(my_list):
            if i == idx:
                my_list.remove(elm)
    return my_list
