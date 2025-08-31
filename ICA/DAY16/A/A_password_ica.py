# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# CS 1112
# Learning Python (Python version: 3)
# Module 3: Loops & Break and Continue ACTIVITY

# Activity: Password Guessing Game with Hints
#
# Objective: Teach students how to create a password guessing game using loops, break, and continue.
#
# Instructions:
#
# Create a program that allows the user to guess a secret password.
# The program should provide hints and give the user multiple attempts to guess correctly.
# If you do not guess correctly within the max attempts, program prints the correct password.
# Use break and continue accordingly.
# Provide the following code template as a starting point:

# =============================================================
## HINTS and idea about the ALGORITHM:
# - Allow the player a maximum number of attempts (e.g., max_attempts=3)
# - Keep track of the current attempt using variable "attempts"
#   (starting with value zero (0) since initially no attempts
#   have been made)
#
# Game loop:
# - As long as the maximum attempts hasn't been reached...
#     - Ask/prompt the user to guess the password
#     - if the guess is matches (is equal to) the secret password,
#       print "Congratulations! You guessed the correct password."
#     - otherwise, print "Incorrect password. Try again."
#       Also increment (increase) the number of attempts by 1
#           - if the number of attempts is >= max_attempts then
#             print "Sorry, you've reached the maximum number of attempts."
#     - Provide a hint after the first failed attempt (when attempts==1)
#       (Type in any hint you want to help the player guess correctly)
#
# End of the game:
# - if the maximum number of attempts was reached (attempts == max_attempts)
#   print the correct password out
# =============================================================


## WRITE YOUR SOLUTION HERE
# (Note: some starter code has been given to you, please build on this.)

# Set the secret password
secret_password = "python123"  # this is the password to be guessed

# Initialize variables
attempts = 0  # current number of attempts
max_attempts = 3  # set the maximum number of attempts, e.g., 3

# Welcome message
print("Welcome to the Password Guessing Game!")

# Start the game loop
# Hint for the while condition:
while ...:
    # Ask/prompt the user to guess the password:
    guess = input("Enter your guess: ")

    # Check if the guess is correct...


    # (else) If the guess isn't correct...



    # Provide a hint after the first failed attempt:




# End of the game
if attempts == max_attempts:
    print("The correct password was:", secret_password)