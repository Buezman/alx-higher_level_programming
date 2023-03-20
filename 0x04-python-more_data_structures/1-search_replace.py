#!/usr/bin/python3

def search_replace(my_list, search, replace):
    result = []

    for x in my_list:
        if (x == search):
            result.append(replace)
        else:
            result.append(x)

    return result
