#!/usr/bin/python3

def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    best = list(a_dictionary.keys())[0]
    score = a_dictionary[first]

    for k, v in a_dictionary.items():
        if v > score:
            best = k
            score = k

    return best
