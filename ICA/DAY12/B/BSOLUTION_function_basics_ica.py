# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 2: Functions Basics ACTIVITY -- SOLUTION

## For each exercise, create a function that accomplishes
## what is described in the requirements

## Function signatures along with the docstring documentation
## are provided for each task!
# (A Python docstring is a string literal used to document a Python
# module, class, function or method, helping programmers
# understand functionality without reading implementation details)

## IMPORTANT: use the Python keyword 'return' followed by the value
##            you want to return (function output) rather than
##            printing the result.

# EXERCISE #1:
# Write a function that computes the area of a triangle

# SOLUTION
def calculate_triangle_area(base, height):
    '''
    Function to compute the area of a triangle
    :param base: measurement of the base of the triangle
    :param height: measurement of the height of the triangle
    :return: the area of the triangle, calculated using base and height
    '''
    area = 0.5 * base * height  # the calculation (Area = 1/2 * base * height)
    return area


# EXERCISE #2:
# Write a function to determine if a number is positive or negative

# SOLUTION
def check_positive_negative(num):
    '''
    Function that determines if a given number is positive or negative
    :param num: the number to be evaluated
    :return: a string, "Positive" or "Negative", based on the sign of the number
    '''
    if num > 0:  # Check if the number is greater than zero
        return "Positive"
    else:  # the number is negative (or zero - could be handled separately if needed)
        return "Negative"


# EXERCISE 3:
# Write a function to determine if a year is a leap year
'''
Note:  Leap years are years divisible by 4, except for century years
       which must be divisible by 400 to be leap years.

       *Century years - 1900, 2000, 2100, etc.
'''


# SOLUTION (two possible solutions -- see slides, as there are others!)
def check_leap_year(year):
    '''
    A function that checks whether a given year is a leap year or not
    :param year: the year to be evaluated
    :return: a Boolean value, True or False, indicating if the given year is a leap year (True) or not (False)
    '''
    # if year is evenly divisible by 4 and not by 100, OR year is evenly divisible by 400, then it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:  # Otherwise, the year is not a leap year
        return False


def check_leap_year2(year):
    '''
    A function that checks whether a given year is a leap year or not
    :param year: the year to be evaluated
    :return: a Boolean value, True or False, indicating if the given year is a leap year (True) or not (False)
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