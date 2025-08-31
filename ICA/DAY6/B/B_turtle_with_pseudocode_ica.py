# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# CS 1112
# Learning Python (Python version: 3)
# Module 1: Turtle with Pseudocode ACTIVITY

### THE FOLLOWING IS SOME PSEUDOCODE.
### FOLLOW THE STEPS TO CONVERT THESE INSTRUCTIONS INTO PYTHON CODE, USING TURTLES.
### BE SURE TO CHECK-IN WITH A TA BEFORE YOU LEAVE CLASS TODAY.

# 1. Import the 'turtle' module.
# 2. Create a 'turtle' object, call the turtle any name that you please (e.g., tobi).
# 3. Use the shape() function to change the shape to a turtle icon.

# 4. Prompt the user to enter the number of EDGES for the spiral
#    (i.e., the number of times the program will draw an edge in the spiral)
#    (store result in variable spiral_edges, and type cast after calling the input function).
# 5. Prompt the user to enter the length of each side
#    (store result in variable side_length, and type cast after calling the input function).

# 6. We will be creating polygon spirals, so set the pivot angle to something
#    appropriate, e.g. 90 degrees for a square, 72 degrees for a pentagon, etc.
#    (use variable angle and set it equal to a number such as 72).
# 7. In order to create a spiral effect, we have to increment (increase)
#    the length of the subsequent line we draw.
#    So, create a variable called length_increment and set it to a small value
#    (e.g., a number between 2 and 5).

# 8. Repeat the following steps until the desired number of sides is reached (use a for-loop that runs spiral_edges times):
#    a. Move the turtle forward by the specified length (side_length).
#    b. Turn the turtle to the right by a fixed angle (e.g., 90 degrees). Use the variable angle.
#    c. Increase the length of each side by a small amount
#       (update side_length using length_increment).
#       (HINT: add length_increment to side_length and store the result back into variable side_length)
#       (This will cause the program to draw a slightly longer line than the last one, to create the spiral effect)

#    Outside of the for loop, do the following: (Remember to UNindent your code! Ask if you are unsure!)
# 9. Hide the turtle (HINT: use .hideturtle() method on your named turtle).
# 10. Pause the program until the user closes the turtle graphics window
#     (HINT: use .done() method on turtle -- NOT on your named turtle, like "tobi").


# WRITE YOUR PYTHON SOLUTION BELOW:
#**************************************************

# Import statement has been provided for you
# and the turtle object has been created and named "tobi" (steps #1 and #2)
import turtle

tobi = turtle.Turtle()  # Feel free to change the name "tobi" to anything that you like! Don't change "turtle.Turtle()"














# Last line of your code: Pause the program  (step #10)
turtle.done()  # Turtle can now rest :-)
# Drawing onto the turtle canvas is complete, ready to close.