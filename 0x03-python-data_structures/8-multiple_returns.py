#!/usr/bin/python3

def multiple_returns(sentence):
    n = len(sentence)

    if n > 0:
        return (n, sentence[0])
    else:
        return(0, None)
