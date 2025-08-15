# CS 1112
# Learning Python (Python version: 3)
# Module 5: Dictionaries Activity

# Student Grade Tracker
# Create a simple student grade tracker using a dictionary.
# Finish coding each option

# For option 1, add a new student and their grade (as a LIST) to student_grades
# (Key = name, which is a string.  Value = grades, which is a List. For example: 'Sage': [80.0, 85.0, 90.0])
#       - prompt the user for the student's name
#       - prompt the user for the student's grades separated by spaces
#       - convert the grades provided into a list   [Hint: consider using the function .split()]
#       - add the key-value pair (name-grades) to the dictionary

# For option 2, calculate the average grades stored in student_grades
#       - prompt the user to enter the student's name to calculate their average grade
#       - check if their name (a key in the dictionary) exists.
#           - If so, calculate the average grade and print it out
#           - If not, print an appropriate message to the user indicating what happened

# For option 3, break out of the loop
#       - the program should stop at this point (no further iterations of the loop)

# Starter Code:
# Create an empty student grade dictionary:
student_grades = {}

while True:  # Continue to run until the user selects option 3, "Quit"
    print("\nMenu:")
    print("1. Add a student and their grades")
    print("2. Calculate average grades")
    print("3. Quit")

    choice = input("Enter your choice: ")

    # todo: Add if-elif-elif-else here

    # WRITE THE REST OF YOUR SOLUTION HERE
