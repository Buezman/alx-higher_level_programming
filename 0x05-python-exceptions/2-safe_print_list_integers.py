#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of integers in a list.

    Args:
        my_list (list): List of elemets to be printed
        x (int): number of elements to be printed

    Returns: The number of elements printed
    """
    ans = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ans += 1
        except (TypeError, ValueError):
            continue

    print("")

    return ans
