#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for k in a_dictionary:
        val = a_dictionary[k] * 2
        a_dictionary.update({k: val})
