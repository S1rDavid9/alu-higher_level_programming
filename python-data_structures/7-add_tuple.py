#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuple_a has at least two elements, filling with 0 if necessary
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    else:
        tuple_a = tuple_a[:2]

    # Ensure tuple_b has at least two elements, filling with 0 if necessary
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    else:
        tuple_b = tuple_b[:2]

    # Add the first elements and the second elements
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result
