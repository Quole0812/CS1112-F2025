# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 2: Booleans and Conditionals ACTIVITY -- SOLUTION

# CONDITIONAL ACTIVITY
# Write code using conditionals that converts a numerical grade
# to its corresponding GPA value. (E.g. if grade = 88, return 3.3)

# Grade Scale:
# 97-100 = A+ = 4.0
# 93-96  = A  = 4.0
# 90-92  = A- = 3.7
# 87-89  = B+ = 3.3
# 83-86  = B  = 3.0
# 80-82  = B- = 2.7
# 77-79  = C+ = 2.3
# 73-76  = C  = 2.0
# 70-72  = C- = 1.7
# 65-69  = D+ = 1.3
# 60-64  = D  = 1.0
# Below 60 = F = 0.0

# @@@@@
# BONUS CHALLENGE:
#       Create a *function* named convert_to_gpa that takes a
#       numerical grade as input and returns the corresponding GPA.
#       Function signature: def convert_to_gpa(numerical_grade):
#       Remember to use conditionals inside your function!
# @@@@@

# Tip: Consider using if...elif...elif...else structure for your conditionals


# SAMPLE SOLUTION: (using a function - function is optional)
def convert_to_gpa(numerical_grade):
    if numerical_grade >= 97 and numerical_grade <= 100:
        return 4.0
    elif numerical_grade >= 93 and numerical_grade <= 96:
        return 4.0
    elif numerical_grade >= 90 and numerical_grade <= 92:
        return 3.7
    elif numerical_grade >= 87 and numerical_grade <= 89:
        return 3.3
    elif numerical_grade >= 83 and numerical_grade <= 86:
        return 3.0
    elif numerical_grade >= 80 and numerical_grade <= 82:
        return 2.7
    elif numerical_grade >= 77 and numerical_grade <= 79:
        return 2.3
    elif numerical_grade >= 73 and numerical_grade <= 76:
        return 2.0
    elif numerical_grade >= 70 and numerical_grade <= 72:
        return 1.7
    elif numerical_grade >= 65 and numerical_grade <= 69:
        return 1.3
    elif numerical_grade >= 60 and numerical_grade <= 64:
        return 1.0
    else:
        return 0.0


### TESTING ###
grade = 88
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

grade = 95
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

grade = 62
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

grade = 75
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

grade = 45
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

grade = 99
print("If grade is " + str(grade) + ": " + str(convert_to_gpa(grade)) + " GPA")

'''
#~Provided you enter these grades, this is what the output should be~#
If grade is 88: 3.3 GPA
If grade is 95: 4.0 GPA
If grade is 62: 1.0 GPA
If grade is 75: 2.0 GPA
If grade is 45: 0.0 GPA
If grade is 99: 4.0 GPA
'''