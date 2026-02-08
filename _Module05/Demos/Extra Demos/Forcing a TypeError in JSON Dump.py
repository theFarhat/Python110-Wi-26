""" This script demonstrates how Python's json module handles correct and incorrect
    data types during serialization with the json.dump() function.

    It shows two cases:
    1. A valid dictionary that is properly serialized to a JSON file.
    2. An invalid data structure that appears to be a dictionary but is actually a set
       containing a single string. This structure causes a TypeError during serialization.

    The purpose of this demo is to help students understand:
        - The importance of using correct data types when working with JSON.
        - How Python interprets different syntaxes (e.g., set vs. dictionary).
        - How to identify and handle serialization errors using try-except blocks.
"""

import json

FILE_NAME = "../TestFile.json"

# Data in a correct JSON format
student_table = {'FirstName': 'Good', 'LastName': 'Data'}

try:
    file = open(FILE_NAME, "w")
    print(student_table, "is of type:", type(student_table))  # This is a dictionary
    json.dump(student_table, file)  # This works correctly and writes to the file
except TypeError as e:
    print("Please check that the data is a valid JSON format\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Data not in a correct JSON format
# This looks like a dictionary, but Python treats it as a set with one string element
student_table = {"'FirstName': 'Bad', 'LastName': 'Data'"}

try:
    file = open(FILE_NAME, "w")
    print(student_table, "is of type:", type(student_table))  # This is actually a set
    json.dump(student_table, file)  # This will raise a TypeError
except TypeError as e:
    print("So you get this error:")
    print("Please check that the data is a valid JSON format\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()
