#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = ""

    if n >= 0:
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
    else:
    #    for i in range(len(str)):
    #        if i != (len(str) + n):
    #            new_str += str[i]
        return str

    return new_str
