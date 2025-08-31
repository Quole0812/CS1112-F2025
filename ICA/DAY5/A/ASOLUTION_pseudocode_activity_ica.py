# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

#Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 1: Pseudocode ACTIVITY

# -- ACTIVITY #1 --
# 1. Prompt the user to enter the first number.
# 2. Store the entered number in a variable called num1.
# 3. Prompt the user to enter the second number.
# 4. Store the entered number in a variable called num2.
# 5. Add num1 and num2, and store the result in a variable called sum.
# 6. Display the sum.

# SAMPLE SOLUTION:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print("The sum is:", sum)

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

total = num1 + num2 + num3
average = total / 3

print("The average is:", average)

# SAMPLE SOLUTION:
# 1. Prompt the user to enter the first number.
# 2. Store the entered number in a variable called num1.
# 3. Prompt the user to enter the second number.
# 4. Store the entered number in a variable called num2.
# 5. Prompt the user to enter the third number.
# 6. Store the entered number in a variable called num3.
# 7. Calculate the sum of num1, num2, and num3, and store the result in a variable called total.
# 8. Calculate the average by dividing total by 3 and store the result in a variable called average.
# 9. Display the average.