#!/usr/bin/python3
from sys import argv

def add_num(*args):
    # define variables:
    total = [0] * (len(max(args, key=len)) + 1)
    rem = 0

    # add number from right to left:
    for i in range(1, (len(total) + 1)):
        sum_digit = rem
        for arg in args:
            if i <= len(arg.lstrip('-')):
                digt = int(arg[-i])
                if arg.startswith('-'):
                    digt = -digt
                sum_digit += digt
        total[-i] = sum_digit % 10
        rem = sum_digit // 10

    if rem:
        total[0] = rem

    # handling the minus numbers:
    if total[0] < 0:
        carry = 1
        for i in range(1, len(total) + 1):
            total[-i] = -total[-i]
            if i > 1:
                total[-i] -= carry
            if total[-i] < 0:
                total[-i] += 10
                carry = 1
            else:
                carry = 0
        
        # remove additional zeros:
        while len(total) > 1 and total[0] == 0:
            total.pop(0)

        # extract numbers from list as string
        result = '-' + ''.join(map(str, total))
    else:
        # remove additional zeros:
        while len(total) > 1 and total[0] == 0:
            total.pop(0)
        
         # extract numbers from list as string    
        result = ''.join(map(str, total))   


    # return the function:
    return result


if __name__ == "__main__":

    try:
        reslt = add_num(*argv[1:])
        print(reslt)
    except:
        print(0)
