# CS 1112
# Learning Python (Python version: 3)
# Module 5: Tuples Activity

# Implement a function named find_median
# Function finds the median of a tuple of numbers, and prints the median found
#   - Find the length of the tuple, and then sort the tuple and convert it to a list
#                                               (Hint: sorted() function - what does it return?)
#   - If the length of the tuple is odd, the median is the middle value
#       For example, if the sorted list was [1, 2, 3, 4, 5], the median is 3
#   - If the length of the tuple is even
#       - Find the middle two numbers, (middle1 and middle2)
#       - Then find the average of these two numbers
#       For example, if the sorted list was [1, 2, 3, 4, 5, 10], middle1=4 and middle2=3, median: 3.5


# WRITE YOUR SOLUTION HERE:

# Function to find the median of a tuple of numbers
def find_median(numbers):
    if not numbers:  # If the list is empty...
        print("No numbers to analyze.")
        return







## TESTING YOUR CODE:
# Tuple of numbers
number_tuple = (5, 3, 1, 4, 2)
number_tuple2 = (5, 3, 1, 4, 2, 10)

# Call the function to find the median
find_median(number_tuple)
find_median(number_tuple2)
