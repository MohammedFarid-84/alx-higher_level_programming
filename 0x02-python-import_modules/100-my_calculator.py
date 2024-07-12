#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
from sys import argv, exit


def doCalc(argvs):
    opr = {'+': add, '-': sub, '*': mul, '/': div}
    if len(argvs) < 4:
        print(f'Usage: {argvs[0]} <a> <operator> <b>')
        exit(1)
    elif argvs[2] not in opr:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        n1 = int(argvs[1])
        n2 = int(argvs[3])
        func = opr[argvs[2]]
        result = func(n1, n2)
        print(f'{n1} {argvs[2]} {n2} = {result}')


if __name__ == "__main__":
    doCalc(argv)
