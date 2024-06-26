#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':  # Check if character is lowercase
            uppercase_char = chr(ord(char) - 32)  # Convert to uppercase using ASCII values
            print(uppercase_char, end="")
        else:
            print(char, end="")
    print()  # Print newline after the string
