#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
my_list1 = []
max_value1 = max_integer(my_list1)
print("Max: {}".format(max_value1))
my_list2 = [-1, -2, -3, -4]
max_value2 = max_integer(my_list2)
print("Max: {}".format(max_value2))
