#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return 0

    my_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = my_dict[roman_string[0]]

    for i in range(1, len(roman_string)):
        key = roman_string[i]
        val = my_dict[key]
        prev = roman_string[i - 1]
        x = my_dict[prev]
        if val > x:
            num += val - (2 * x)
        else:
            num += val

    return num
