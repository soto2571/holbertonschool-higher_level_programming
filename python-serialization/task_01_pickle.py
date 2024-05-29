#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Parameters:
        filename (str): The filename where the object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}")
        except Exception as e:
            print(f"Error serializing object to file: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Parameters:
        filename (str): The filename from which the object will be loaded.

        Returns:
        CustomObject: The deserialized object instance.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            print(f"Object deserialized from {filename}")
            return obj
        except Exception as e:
            print(f"Error deserializing object from file: {e}")
            return None
