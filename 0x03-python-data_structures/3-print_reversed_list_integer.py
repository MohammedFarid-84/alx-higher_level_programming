#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse()
        print('\n'.join('{:d}'.format(i) for i in my_list))
