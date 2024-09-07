#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    lsts = []
    for i in range(0, len(matrix)):
        lstx = list(map(lambda x: x ** 2, matrix[i]))
        lsts.append(lstx)

    return lsts
