# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 3: Debugging & Style ACTIVITY

# PRINT DEBUGGING
# below is an example of an incorrect power function
def power(b, e):
    for i in range(e):
        b+=e
    return b
# use print statement debugging to determine what is wrong and fix the function
# sample debugging
def power(b, e):
    for i in range(e):
        b+=e
    correct = b**e
    print("Code output: b")
    print("Correct output: " + correct)
    return b
# the two print statements compare the two outputs, if the code output is wrong
# ***** Give them a hint wit te range of lines that they should look at

# STYLE
# Below is a function that does not have the right style
def calculateAverage(numbers):
result=0
for number in numbers:
result+=number
average=result/len(numbers)
if average>5:
print("Above average")
else:
print("Below average")

# Fix this function so that there are no errors, so that the style is correct!

# SOLUTION
def calculate_average(numbers):
    result = 0
    for number in numbers:
        result += number
    average = result / len(numbers)
    if average > 5:
        print("Above average")
    else:
        print("Below average")