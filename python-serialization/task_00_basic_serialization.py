#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a dictionary and save it to a JSON file.

    Parameters:
    data (dict): The dictionary to serialize.
    filename (str): The JSON file to save to. Existing file will be replaced.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Parameters:
    filename (str): The JSON file to read from.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded from {filename}")
        return data
    except Exception as e:
        print(f"Error loading data from file: {e}")
        return None
