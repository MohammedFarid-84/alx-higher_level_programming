#!/usr/bin/python3


def remove_char_at(str, n):
    new_str = ""

    if n >= 0:
        for i in range(len(str)):
            if i != n:
                new_str += str[i]
    else:
        return str

    return new_str
