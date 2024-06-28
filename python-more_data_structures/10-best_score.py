#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    max_score = float('-inf')  # Start with negative infinity to handle all negative scores

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score:
            max_score = value
            best_key = key

    return best_key
