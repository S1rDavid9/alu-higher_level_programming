#!/usr/bin/python3

if __name__ == "__main__":

import sys
   argv = sys.argv[1:]  # Get the arguments excluding the script name
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
