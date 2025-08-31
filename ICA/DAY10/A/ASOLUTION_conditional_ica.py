# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 2: Booleans and Conditionals ACTIVITY -- SOLUTION


# CONDITIONAL ACTIVITY
# Use conditionals to write some code that converts and returns
# the GPA when given a percentage. (E.g. if percentage = 95, return 4.0)

# 94-100 = A = 4.0
# 90-93 = A- = 3.7
# 87-89 = B+ = 3.3
# 83-86 = B = 3.0
# 80-82 = B- = 2.7
# 77-79 = C+ = 2.3
# 73-76 = C = 2.0
# 70-72 = C- = 1.7
# 67-69 = D+ = 1.3
# 63-67 = D = 1.0
# 60-62 = D- = 0.7
# 0-59 = F = 0.0

# @@@@@
# Want a challenge?
#       Write a *function* called gpa_calc that converts and
#       returns the GPA when given a percentage.
#       Use this function definition:  def gpa_calc(percent):
#       You will still use conditionals inside this function.
# @@@@@

# Hint: For conditionals think about the if...elif...elif...else structure


# SAMPLE SOLUTION: (using a function - function is optional)
def gpa_calc(percent):
    if percent >= 94 and percent <= 100:
        return 4.0
    elif percent >= 90 and percent <= 93:
        return 3.7
    elif percent >= 87 and percent <= 89:
        return 3.3
    elif percent >= 83 and percent <= 86:
        return 3.0
    elif percent >= 80 and percent <= 82:
        return 2.7
    elif percent >= 77 and percent <= 79:
        return 2.3
    elif percent >= 73 and percent <= 76:
        return 2.0
    elif percent >= 70 and percent <= 72:
        return 1.7
    elif percent >= 67 and percent <= 69:
        return 1.3
    elif percent >= 63 and percent <= 66:
        return 1.0
    elif percent >= 60 and percent <= 62:
        return 0.7
    else:
        return 0.0


### TESTING ###
percentage = 87
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

percentage = 92
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

percentage = 61
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

percentage = 76
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

percentage = 50
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

percentage = 99
print("If percentage is " + str(percentage) + ": " + str(gpa_calc(percentage)) + " GPA")

'''
#~Provided you enter these percentages, this is what the output should be~#
If percentage is 87: 3.3 GPA
If percentage is 92: 3.7 GPA
If percentage is 61: 0.7 GPA
If percentage is 76: 2.0 GPA
If percentage is 50: 0.0 GPA
If percentage is 99: 4.0 GPA
'''