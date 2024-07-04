#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
        count += 1
    print("")  # for new line
    return printed
