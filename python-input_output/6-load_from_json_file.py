#!/usr/bin/python3
"""
Writing a function that creates an object from a JSON
"""

import json


def load_from_json_file(filename):
    """
    This function creates an object from a json file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
