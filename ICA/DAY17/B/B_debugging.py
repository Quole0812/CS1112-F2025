# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 3: Debugging & Style ACTIVITY -- SOLUTION

# PRINT DEBUGGING
# below is an example of an incorrect power function
def power(b, e):
    for i in range(e):w
        b += e
    return b


# use print statement debugging to determine what is wrong and fix the function

# DEBUGGING SOLUTION:
def power_debug(b, e):
    original_b = b  # store original base value
    print(f"Starting with base = {b}, exponent = {e}")

    for i in range(e):
        print(f"Iteration {i}: b before += operation: {b}")
        b += e
        print(f"Iteration {i}: b after += operation: {b}")

    correct = original_b ** e
    print(f"Code output: {b}")
    print(f"Correct output: {correct}")
    return b


# ANALYSIS: The bug is that we're adding the exponent (e) to the base (b) instead of multiplying
# The correct power function should multiply b by itself e times, not add e to b repeatedly

# CORRECTED POWER FUNCTION:
def power_fixed(b, e):
    result = 1
    for i in range(e):
        result *= b
    return result


# Alternative correct solution using built-in operator:
def power_fixed_alt(b, e):
    return b ** e


# STYLE
# Below is a function that does not have the right style
def calculateAverage(numbers):
    result = 0


for number in numbers:
    result += number
average = result / len(numbers)
if average > 5:
    print("Above average")
else:
    print("Below average")


# Fix this function so that there are no errors, so that the style is correct!

# STYLE SOLUTION:
def calculate_average(numbers):
    result = 0
    for number in numbers:
        result += number
    average = result / len(numbers)
    if average > 5:
        print("Above average")
    else:
        print("Below average")