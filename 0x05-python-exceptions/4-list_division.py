#!/usr/bin/python3
# 4-list_division.py

def list_division(my_list_1, my_list_2, list_length):
    """Division of two lists by elements.

    Args:
        my_list_1 (list): numerator list
        my_list_2 (list): denominator list
        list_length (int): length of list

    Returns: new list of division of lists 1 and 2
    """
    result = []

    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)

    return (result)
