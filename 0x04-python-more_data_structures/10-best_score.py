#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highestscore = 0  # Will store the highest score

    for keys, value in a_dictionary.items():
        if value > highestscore:
            highestscore = value
            highestscorer = keys

    return highestscorer
