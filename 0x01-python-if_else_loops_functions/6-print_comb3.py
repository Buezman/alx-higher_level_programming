#!/usr/bin/python3
for i in range(0, 10):
    if i == 9:
        break
    for j in range((i + 1), 10):
        if i == 8 and j == 9:
            print("{}".format(89))
            break
        print("{}{}".format(i, j), end=", ")
