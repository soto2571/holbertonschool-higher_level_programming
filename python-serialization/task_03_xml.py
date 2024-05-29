#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to a file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The filename to save the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"Dictionary serialized to {filename}")
    except Exception as e:
        print(f"Error serializing dictionary to XML: {e}")


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.

    Parameters:
    filename (str): The filename to read the XML data from.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {child.tag: child.text for child in root}
        print(f"Data deserialized from {filename}")
        return dictionary
    except Exception as e:
        print(f"Error deserializing XML to dictionary: {e}")
        return None
