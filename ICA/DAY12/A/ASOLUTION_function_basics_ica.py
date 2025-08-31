# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 2: Functions Basics ACTIVITY -- SOLUTION

## For each activity, write a function that accomplishes
## what is stated in the description

## Function definitions along with the docstring comment header
## is provided for each!
# (A Python docstring is a string used to document a Python
# module, class, function or method, so programmers can
# understand what it does without having to read the details
# of the implementation)

## REMEMBER: use the Python key word 'return' followed by the thing
##           you want to return (output of the function) instead of
##           printing the result.

# ACTIVITY #1:
# Write a function that calculates the perimeter of a rectangle

# SOLUTION
def calculate_rectangle_perimeter(length, width):
    '''
    Function to calculate the perimeter of a rectangle
    :param length: measurement of the length of the rectangle
    :param width:  measurement of the width of the rectangle
    :return: the perimeter of the rectangle, calculated using length and width
    '''
    perimeter = 2 * (length + width)  # the calculation
    return perimeter


# ACTIVITY #2:
# Write a function to check if a number is even or odd

# SOLUTION
def check_even_odd(number):
    '''
    Function that checks if a given number is even or odd
    :param number: the number to be checked
    :return: a string, "Even" or "Odd", depending on if the number is even or odd
    '''
    if number % 2 == 0:  # Using modulus to determine if the number is even
        return "Even"
    else:  # the numher is odd
        return "Odd"


# ACTIVITY 3:
# Write a function to check if a year is a leap year
'''
Note:  Leap years are non-end-of-century years that are divisible by 4,
       or end-of-century-year that are divisible by 400.

       *End of century years - 2000, 3000, etc.
'''


# SOLUTION (two possible solutions -- see slides, as there are others!)
def is_leap_year(year):
    '''
    A function that determines if a given year is a leap year or not
    :param year: the year to be checked
    :return: a Boolean, True or False, determining if the given year is a leap year (True) or not (False)
    '''
    # if year is evenly divisible by 4 and not by 100, OR year is evenly divisible by 400, then it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:  # Otherwise, the year is not a leap year
        return False


def is_leap_year2(year):
    '''
    A function that determines if a given year is a leap year or not
    :param year: the year to be checked
    :return: a Boolean, True or False, determining if the given year is a leap year (True) or not (False)
    '''
    div4 = ((year % 4) == 0)
    div100 = ((year % 100) == 0)
    div400 = ((year % 400) == 0)

    if div400:  # if year evenly divisible by 400, then True
        return True
    elif div100:  # if year evenly divisible by 100, then False
        return False
    elif div4:  # if year evenly divisible by 4, then True (if we got here, year was not divisible by 100)
        return True
    else:
        return False  # Otherwise, False