#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        printed = 0
        while count < x and count < len(my_list):
            print("{:d}".format(my_list[count]), end="")
            printed += 1
            count += 1
        print("")  # print newline at the end
        return printed
    except (ValueError, TypeError):
        pass
