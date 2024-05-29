#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save to data.json.

    Parameters:
    csv_filename (str): The filename of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data from {csv_filename} has been converted to data.json")
        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
