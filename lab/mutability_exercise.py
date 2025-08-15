# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 2: String Mutability
## Example taken from codehs.com

## WITHOUT RUNNING THE FILE... which line (LINE 15 or LINE 16) will cause an error??

my_string = "karel"

# One of the two lines below will cause an error.
# Each line is an attempt to replace the first
# letter of myString with H.
#
# Comment out the line you think is incorrect: (put a # at the beginning of the line you think is incorrect)
#my_string[0] = "K"                  ## LINE 15
my_string = "K" + my_string[1:]     ## LINE 16

print(my_string)

## Once you guessed, run the file. Were you correct?
## Please ask a TA or your professor if you have questions about why an error occured.



## Note: This is not a regular in-class activity (no need to check-in with a TA!)






# 
# Answer: Option 2
#
# Reasoning: Strings are immutable!
#       Once a string is created, it cannot be changed
#       You attempted to modify a string
#