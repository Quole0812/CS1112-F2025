
# PA06: Class Finder starter code
# CS 1112: Introduction to Programming, Fall 2024

# NAME: TODO:Add your name here
# COMPUTING ID: TODO: Add your email/computing ID here
# PA NUMBER and NAME: PA06: Class Finder
# Resources used (if applicable): TODO: Add here all resources used, OR say that you didn't use any resources

# Starter code original author: Paul Karhnak (many thanks!)

# ~~ Important notice: ~~
##   You MUST include the entire "courses_dict" dictionary in the file for Gradescope to run all tests!!

# Dictionary with list entries.

# Format: {"Course code-section": ["Full name", "Type", "Instructor", "Meeting days", start time (int), end time(int) "Meeting place", credits (int), seats available (int)]}
courses_dict = {
    "CS 1010-001": ["Introduction to Information Technology", "Lecture", "David Evans", "Tu/Th", 1100, 1215,
                    "Olsson 009", 3, 45, 80],
    "CS 1110-001": ["Introduction to Programming", "Lecture", "Arohi Khargonkar", "Mo/We/Fr", 1000, 1050, "Gilmer 301",
                    3, 295, 300],
    "CS 1110-002": ["Introduction to Programming", "Lecture", "Arohi Khargonkar", "Mo/We/Fr", 1300, 1350, "Rice 130", 3,
                    143, 145],
    "CS 1110-003": ["Introduction to Programming", "Lecture", "Derrick Stone", "Mo/We/Fr", 1200, 1250, "Olsson 120", 3,
                    145, 145],
    "CS 1110-100": ["Introduction to Programming", "Lab", "Arohi Khargonkar", "Th", 930, 1045, "Olsson 018", 3, 83, 85],
    "CS 1110-101": ["Introduction to Programming", "Lab", "Arohi Khargonkar", "Th", 1100, 1215, "Olsson 018", 3, 75,
                    85],
    "CS 1110-102": ["Introduction to Programming", "Lab", "Arohi Khargonkar", "Th", 1230, 1345, "Olsson 018", 3, 82,
                    85],
    "CS 1111-001": ["Introduction to Programming", "Lecture", "Panagiotis Apostolellis", "MoWe", 1400, 1515,
                    "Thornton E316", 3, 75, 80],
    "CS 1112-001": ["Introduction to Programming", "Lecture", "Nada Basit", "Mo/We/Fr", 1230, 1345, "Olsson 018", 3, 90,
                    90],
    "CS 1112-002": ["Introduction to Programming", "Lecture", "Nada Basit", "Mo/We/Fr", 1400, 1515, "Olsson 018", 3, 89,
                    90],
    "CS 2100-001": ["Data Structures and Algorithms 1", "Lecture", "Briana Morrison", "Mo/We/Fr", 1200, 1250,
                    "Chemistry 402", 4, 292, 400],
    "CS 2100-002": ["Data Structures and Algorithms 1", "Lecture", "Derrick Stone", "Mo/We/Fr", 1100, 1150,
                    "Olsson 120", 4, 144, 145],
    "CS 2100-101": ["Data Structures and Algorithms 1", "Lab", "Briana Morrison", "Mo", 1500, 1645, "Olsson 120", 0,
                    125, 125],
    "CS 2100-102": ["Data Structures and Algorithms 1", "Lab", "Briana Morrison", "Mo", 1700, 1845, "Rice 130", 0, 146,
                    150],
    "CS 2120-001": ["Discrete Math and Theory 1", "Lecture", "Elizabeth Orrico", "Mo/We/Fr", 1400, 1450, "Rice 130", 3,
                    129, 130],
    "CS 2120-002": ["Discrete Math and Theory 1", "Lecture", "Elizabeth Orrico", "Mo/We/Fr", 1500, 1550, "Rice 130", 3,
                    130, 130],
    "CS 2120-003": ["Discrete Math and Theory 1", "Lecture", "Elizabeth Orrico", "Mo/We/Fr", 1600, 1650, "Rice 130", 3,
                    130, 130],
    "CS 2130-001": ["Computer Systems and Organization 1", "Lecture", "Daniel Graham", "Mo/We/Fr", 1400, 1450,
                    "Chemistry 402", 4, 391, 400],
    "CS 2130-101": ["Computer Systems and Organization 1", "Lab", "Daniel Graham", "Tu", 930, 1045, "Olsson 018", 0, 73,
                    80],
    "CS 2130-102": ["Computer Systems and Organization 1", "Lab", "Daniel Graham", "Tu", 1100, 1215, "Olsson 018", 0,
                    63, 80],
    "CS 3100-001": ["Data Structures and Algorithms 2", "Lecture", "Robbie Hott", "Tu/Th", 930, 1045, "Rice 130", 3,
                    128, 150],
    "CS 3100-002": ["Data Structures and Algorithms 2", "Lecture", "Raymond Pettit", "Tu/Th", 1400, 1515, "Warner 209",
                    3, 225, 250],
    "CS 3130-001": ["Computer Systems and Organization 2", "Lecture", "Charles Reiss", "Tu/Th", 1530, 1645,
                    "Wilson 402", 4, 294, 300],
    "CS 3130-101": ["Computer Systems and Organization 2", "Lab", "Charles Reiss", "We", 1400, 1515,
                    "Mechanical Engineering Building 339", 0, 68, 72],
    "CS 3130-102": ["Computer Systems and Organization 2", "Lab", "Charles Reiss", "We", 1400, 1515, "Olsson 018", 0,
                    79, 80],
    "CS 3130-103": ["Computer Systems and Organization 2", "Lab", "Charles Reiss", "We", 1530, 1645, "Olsson 018", 0,
                    80, 80],
    "CS 3130-104": ["Computer Systems and Organization 2", "Lab", "Charles Reiss", "We", 1700, 1815, "Olsson 018", 0,
                    12, 80],
    "CS 3710-001": ["Introduction to Cybersecurity", "Lecture", "Angela Orebaugh", "Mo/We/Fr", 1200, 1250, "Gilmer 301",
                    3, 289, 325],
    "CS 4414-001": ["Operating Systems", "Lecture", "Felix Lin", "Tu/Th", 1400, 1515, "Olsson 120", 3, 145, 145],
    "CS 4630-001": ["Defense Against the Dark Arts", "Lecture", "Jack Davidson", "Mo/We", 1530, 1645, "Olsson 009", 3,
                    52, 75],
    "CS 4750-001": ["Database Systems", "Lecture", "Upsorn Praphamontripong", "Mo/We/Fr", 1200, 1250, "Rice 130", 3,
                    141, 145],
    "CS 4760-001": ["Network Security", "Lecture", "Aaron Bloomfield", "Mo/We/Fr", 1000, 1050, "Olsson 018", 3, 32, 75]
}  ## DO NOT DELETE THIS DICTIONARY (or any part of it)!!
   ## Keep this (all of it) in your file when you submit to Gradescope.

# =========================================================================================
### Don't forget multi-line docstring comments for each function
### as well as general in-line comments!
### Example multi-line docstring comment is provided for you in the first function
### Please add multi-line docstring comments to each of your other functions.
# =========================================================================================

# Does class have an associated lab or not (bool)?
# Note: this function has the bare-bones structure of the multi-line docstring comment
def class_has_lab(class_name):
    '''
    Add function description here
    :param class_name: (type) (description)
    :return: (type) (description)
    '''
    # TODO: finish this function!
    return True  # Edit as appropriate

# Return the number of available seats based on the given class_key
# (key in the dictionary corresponding to a distinct class section.
# If invalid key passed, return 0 (can't have seats available for a class which doesn't exist)..
def available_seats(class_key):
    # TODO: finish this function! ** Also, ADD multi-line docstring comment at the top of the function **
    return 0  # Edit as appropriate


# Fetch (first) key in dictionary from formal class name based
# on whether (e.g. "CS 3130-001" from "Computer Systems and Organization 2")
# If improper name passed, should return an empty string.
def lookup_by_name(class_name):
    # TODO: finish this function! ** Also, ADD multi-line docstring comment at the top of the function **
    return ""  # Edit as appropriate

# Return a boolean value based on whether the professor is teaching
# a given class (default: any class) next semester.
def professor_teaches(professor, class_name="any"):
    # TODO: finish this function! ** Also, ADD multi-line docstring comment at the top of the function **
    return False  # Edit as appropriate

# Do the classes conflict or not (bool)? Check the dictionary and see.
def class_conflict(first_class_key, second_class_key):
    # TODO: finish this function! ** Also, ADD multi-line docstring comment at the top of the function **
    return True  # Edit as appropriate


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# =====
# Given a list of class keys (e.g., "CS 1112-001", "CS 2130-105", "CS 4414-001"), attempt to create a
# schedule without conflicts.
# NOTE: You do not need to add to this function directly (though you will need to modify the
# functions it calls to produce the intended output - i.e., the functions above).
# You may add to this function as you wish to try to implement new features and challenge yourself.
# Again, though, this is NOT necessary.
def build_schedule(class_key_list):
    # Initialize a schedule to an empty list.
    # This function will return a list of keys in a schedule that correspond to distinct classes.
    schedule = []

    # Argument format example: ["CS 2100-001", "CS 2120-001", "CS 2130-001"], etc.
    # For each class in the list which is passed in as an argument...
    for new_class_key in class_key_list:
        if new_class_key not in courses_dict.keys():  # If key can't be found, don't do anything with schedule; just continue
            print("WARNING: Class not found for current key.")
            continue

        # If:
        # 1. The key is in the dictionary; AND
        # 2. The schedule is empty; AND
        # 3. The class the key refers to has open seats;
        # 4. THEN enroll. We don't need other checks here since schedule is initially empty (new class can't conflict with anything)
        elif (new_class_key in courses_dict.keys()) and (len(schedule) == 0) and (available_seats(new_class_key) > 0):
            schedule.append(
                new_class_key)  # Append without any other checks (our list is initially empty, so it's fine in this specific case.

        # Otherwise, our schedule is NOT empty, and we need to do additional checks to make sure we don't have class conflicts.
        else:
            for current_key in schedule:
                # Iterate through schedule: we need to check for conflicts with **any** class we previously added.
                if class_conflict(current_key, new_class_key):
                    print("ERROR: Class", current_key, "already in schedule conflicts with new class", new_class_key)
                    return schedule  # Return the partially constructed schedule as-is. We can't proceed further since the requested class conflicts with at least one class already in our schedule.

            if (available_seats(new_class_key) == 0):
                print("ERROR: Class", new_class_key, "has no available seats.")
                return schedule  # Return the partially constructed schedule as-is. We can't proceed further since the requested class has no available seats.
            schedule.append(new_class_key)

    return schedule



if __name__ == '__main__':

# TODO: add any desired tests HERE to prove your code works.

# if __name__ == '__main__' is a statement that says "only run this part of the code if this program is
# being run 'directly'" (i.e., not imported).

# Helpful since you can add any tests here you like, but they shouldn't actually run when you upload
# your submission to Gradescope.

# As such, you can test here without needing to remember to comment things out.
