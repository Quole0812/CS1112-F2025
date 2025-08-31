# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# CS 1112
# Learning Python (Python version: 3)
# Module 2: import ACTIVITY -- SOLUTION

# Properly use import
# Write test code that checks if the functions in sphere.py (area() and volume()) work as intended
# (Call each function at least once and print the output)

# Choose one of the import types and call the methods in sphere.py appropriately


# Sample solution:
# from sphere import *
import sphere

radius = int(input("Enter the radius of the sphere: "))

# No need for including module name when using   from sphere import *
#print("The area is " + str(area(radius)))
#print("The volume is " + str(volume(radius)))

# Using fully qualified name when using:   import sphere
print("The area is " + str(sphere.area(radius)))
print("The volume is " + str(sphere.volume(radius)))