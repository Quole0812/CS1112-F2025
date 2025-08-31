# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 3: Loops ACTIVITY -- SOLUTION

# Activity: Counting even integers in two ways -- using a for-loop and a while-loop
#
# Objective: Write the solution to the same problem using two different approaches: one with a for-loop, and one
#            with a while loop
#
# Instructions:
'''
Write a Python program that counts the number of even integers between two given numbers, inclusive.
(For example, the number of even numbers between 1 and 10 is 5.)

Solve this problem in two ways: one by using a for-loop, and one by using a while-loop.

The two functions you will write are:
  - count_even_numbers_for(start, end)
  - count_even_numbers_while(start, end)

Write a Python program that has function using loops to find and prints all prime numbers within a given range.

Test your code by calling each method and providing various start and end inputs. Confirm the results.
'''

## SOLUTION

# Using a while loop
def count_even_numbers_while(start, end):
    '''
    This function uses a while-loop to count the number of even integers between two numbers.
    :param start: an int, representing the beginning of the range of numbers where even numbers are counted (inclusive)
    :param end: an int, representing the end of the range of numbers where even numbers are counted (inclusive)
    :return: count, an int, that represents the total number of even integers between "start" and "end" (inclusive)
    '''
    # initialize some variables
    count = 0
    current = start

    # while-loop:
    while current <= end:
        if current % 2 == 0:
            count += 1
        current += 1

    # return the result in the variable count
    return count


# Using a for loop
def count_even_numbers_for(start, end):
    '''
    This function uses a for-loop to count the number of even integers between two numbers.
    :param start: an int, representing the beginning of the range of numbers where even numbers are counted (inclusive)
    :param end: an int, representing the end of the range of numbers where even numbers are counted (inclusive)
    :return: count, an int, that represents the total number of even integers between "start" and "end" (inclusive)
    '''
    # initialize the count variable
    count = 0

    # for-loop:
    for num in range(start, end + 1):
        if num % 2 == 0:
            count += 1

    # return the result in the variable count
    return count


# TEST the functions
# (Play around with various start and end values. Here, one test is starting at 1 and ending at 10)
start = 1
end = 10

print("Using while loop:")
print(f"Number of even numbers between {start} and {end}: {count_even_numbers_while(start, end)}")

print("\nUsing for loop:")
print(f"Number of even numbers between {start} and {end}: {count_even_numbers_for(start, end)}")