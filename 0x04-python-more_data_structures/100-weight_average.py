#!/usr/bin/python3

def weight_average(my_list=[]):
    if (not isinstance(my_list, list) or len(my_list) == 0):
        return 0

    sum_weight = 0
    sum_score = 0

    for i in range(len(my_list)):
        score = my_list[i][0]
        weight = my_list[i][1]

        sum_score += score * weight
        sum_weight += weight

    return (sum_score / sum_weight)
