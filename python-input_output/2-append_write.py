#!/usr/bin/python3
"""
Writing a function that appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end
    of a text file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
