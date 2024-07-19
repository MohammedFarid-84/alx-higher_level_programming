#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    if tuple_a and tuple_b:
        for i in range(0, 2):
            if len(tuple_a) == len(tuple_b):
                x = tuple_a[i]
                y = tuple_b[i]
            elif len(tuple_a) > len(tuple_b):
                x = tuple_a[i]
                y = tuple_b[i] if i < len(tuple_b) else 0
            else:
                x = tuple_a[i] if i < len(tuple_a) else 0
                y = tuple_b[i]
            z = x + y
            new_tuple.append(z)
    elif tuple_a:
        new_tuple.append(tuple_a)
    elif tuple_b:
        new_tuple.append(tuple_b)
    return tuple(new_tuple)
