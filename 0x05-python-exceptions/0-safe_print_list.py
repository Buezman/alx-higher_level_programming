#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """Prints x elements in a list.

    Args:
        my_list (list): List of elemets to be printed
        x (int): number of elements to be printed

    Returns: The number of elements printed
    """
    ans = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ans++
        except IndexError:
            break

    print("")

    return ans
