#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0 and my_list != None:
        my_list.reverse()
        print('\n'.join('{:d}'.format(i) for i in my_list))
