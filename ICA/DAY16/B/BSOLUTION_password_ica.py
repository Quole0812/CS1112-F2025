# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 3: Loops & Break and Continue ACTIVITY -- SOLUTION

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
#       (Afterward you should stop and exit the loop. Remember how to do this?)
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


# SOLUTION
# Set the secret password
secret_password = "python123"  # this is the password to be guessed

# Initialize variables
attempts = 0  # current number of attempts
max_attempts = 3  # set the maximum number of attempts, e.g., 3

# Welcome message
print("Welcome to the Password Guessing Game!")

# Start the game loop
while attempts < max_attempts:
    guess = input("Enter your guess: ")

    # Check if the guess is correct
    if guess == secret_password:
        print("Congratulations! You guessed the correct password.")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
        if attempts >= max_attempts:
            print("Sorry, you've reached the maximum number of attempts.")
            continue  # this line is not necessarily needed, but is part of break and continue

    # Provide a hint after the first failed attempt
    if attempts == 1:
        print("Hint: The password contains the word 'python' and some digits.")

# End of the game
if attempts == max_attempts:
    print("The correct password was:", secret_password)