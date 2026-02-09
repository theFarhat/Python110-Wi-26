# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   mofarhat,2/8/2026,Created script from Assignment05-Starter.Py
# ------------------------------------------------------------------------------------------ #

# Import the json and _io modules

import json
import _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data as a Dictionary.
students: list = []  # a table of student data.
file = _io.TextIOWrapper  # Holds a reference to an opened file using _io.TextIOWrapper instead of None
menu_choice: str = '' # Hold the choice made by the user.


# When the program starts, read the file data into a dictionary using json.load, with error handling for FileNotFound.
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

#    for row in file.readlines():
#        # Transform the data from the file
#        student_data = row.split(',')
#        student_data = [student_data[0], student_data[1], student_data[2].strip()]
#        # Load it into our collection (list of lists)
#        students.append(student_data)
#    file.close()

except FileNotFoundError as error:
    print(f'File not found, please ensure {FILE_NAME} exists!\n')
    print('--- Technical Error Message ---\n')
    print(error)
    print(type(error))
    print(error.__doc__)
    print(error.__str__())

except Exception as e:
    print("There was a non-specific error!\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == '1':  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        course_name = input("Please enter the name of the course: ")
        student_data = {'First Name' : student_first_name, 'Last Name' : student_last_name, 'Course Name' : course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print('-'*50)
        for student in students:
    #        print(f'student {student[0]} {student[1]} is enrolled in {student[2]}\n')
            print(f'{student}\n')
        print('-'*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
    #    for student in students:
    #        csv_data = f"{student[0]},{student[1]},{student[2]}\n"
    #        file.write(csv_data)
            file.close()

        except FileNotFoundError as error:
            print(f'File not found, please ensure {FILE_NAME} exists!\n')
            print('--- Technical Error Message ---\n')
            print(error)
            print(type(error))
            print(error.__doc__)
            print(error.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')

        print("The following data was saved to file!")
        for student in students:
            print(f'{student}\n')
        #    print(f"Student {student[0]} {student[1]} is enrolled in {student[2]}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
