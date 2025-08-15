# CS 1112
# Learning Python (Python version: 3)
# Module 6: File Reading with regEx Practice


# Write a Python program that reads a text file, counts the occurrences of EACH word (ignore case) and prints the result.
# Use regular expressions to handle punctuation and ensure accurate word counting.

# Tips:
# Open and read the contents of the text file.
# Use regular expressions to split the text into words, handling punctuation.
# Count the occurrences of each word (ignoring case).
# Print the word count.


# WRITE YOUR SOLUTION HERE:

import re
def word_count(file_path):
    # Open and read the contents of the text file
    # (Hint: while there are many ways you can do this,
    #  perhaps use .read() on your file variable to read in everything)




    # Use regular expressions to split the text into words, handling punctuation
    # (Hint: use re.findall().)



    # Count the occurrences of each word
    # (Hint: how can you keep track of unique words and assocated counts?)




    # Print the word count
    print("")



# Example usage
file_path = 'ica_sample_text.txt'
word_count(file_path)
