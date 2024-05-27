#!/usr/bin/python3

"""
Writing a function that writes a string to a text file
"""


def write_file(filename="", text=""):

    """
    This function writes a string to a text file
    """

    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
