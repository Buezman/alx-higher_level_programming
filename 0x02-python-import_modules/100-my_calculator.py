#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    n = len(sys.argv) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.arg[1])
    b = int(sys.arg[3])

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] in list(ops.keys()):
        print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
