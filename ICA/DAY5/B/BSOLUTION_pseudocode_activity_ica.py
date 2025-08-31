# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 1: Pseudocode ACTIVITY

# -- ACTIVITY #1 --
# 1. Prompt the user to enter the first number.
# 2. Store the entered number in a variable called num1.
# 3. Prompt the user to enter the second number.
# 4. Store the entered number in a variable called num2.
# 5. Subtract num1 and num2, and store the result in a variable called sum.
# 6. Display the sum.

# SAMPLE SOLUTION:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 - num2
print("The total is:", result)

#===================================================================================

# -- ACTIVITY #2 --
# 1. Prompt the user to enter a number.
# 2. Store the entered number in a variable called num.
# 3. If num is greater than 0, display "The number is positive."
# 4. If num is less than 0, display "The number is negative."
# 5. If num is equal to 0, display "The number is zero."

# SAMPLE SOLUTION:
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#===================================================================================

# -- ACTIVITY #3 -- CODE TO PSEUDOCODE
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

total = num1 + num2 + num3 + num4
average = total / 4

print("The average is:", average)

# SAMPLE SOLUTION:
# 1. Prompt the user to enter the first number.
# 2. Store the entered number in a variable called num1.
# 3. Prompt the user to enter the second number.
# 4. Store the entered number in a variable called num2.
# 5. Prompt the user to enter the third number.
# 6. Store the entered number in a variable called num3.
# 5. Prompt the user to enter the fourth number.
# 6. Store the entered number in a variable called num4.
# 7. Calculate the sum of num1, num2, num3, and num 4 and store the result in a variable called total.
# 8. Calculate the average by dividing total by 4 and store the result in a variable called average.
# 9. Display the average.