#!/usr/bin/python3
def element_at(my_list, idx):
    # Check if the index is within the valid range
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
