#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if len(my_list) > 0:
        print('\n'.join('{:d}'.format(i) for i in my_list))
