#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}

    for k in a_dictionary:
        val = a_dictionary[k] * 2
        new_dict.update({k: val})

    return new_dict
