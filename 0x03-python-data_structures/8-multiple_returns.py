#!/usr/bin/python3
def multiple_returns(sentence):

    el1 = len(sentence)
    el2 = sentence[0] if el1 > 0 else None
    tpl = (el1, el2)
    
    return tpl
