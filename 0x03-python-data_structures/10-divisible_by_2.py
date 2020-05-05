#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        judgement = []
        for elements in range(len(my_list)):
            if my_list[elements] % 2 == 0:
                judgement = judgement + [True]
            else:
                judgement = judgement + [False]
        return judgement
