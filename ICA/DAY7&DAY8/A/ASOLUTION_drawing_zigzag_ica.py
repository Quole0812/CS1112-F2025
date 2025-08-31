# *** THIS ICA IS FOR SECTION 001 CS 1112 12:30-1:45 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# Nada Basit
# basit@virginia.edu
# Learning Python (Python version: 3)
# Module 1: Turtle with conditionals ACTIVITY -- SOLUTION

### Create a turtle that draws a zig-zag line.
### THE APPROACH WE WISH YOU TO TAKE IS AS FOLLOWS:
###   - CREATE A FOR-LOOP THAT GOES THROUGH NUMBERS 1 THROUGH 10
###   - IF THE CURRENT NUMBER IS EVEN, MOVE FORWARD 35 PIXELS
###     AND PIVOT RIGHT BY 45 DEGREES
###   - IF THE CURRENT NUMBER IS ODD, MOVE FORWARD 35 PIXELS
###     AND PIVOT *LEFT* BY 45 DEGREES

### FEEL FREE TO BE CREATIVE IN ANY OTHER WAY WITH RESPECT
### TO COLORS AND PENWIDTH, ETC.

### BE SURE TO CHECK-IN WITH A TA BEFORE YOU LEAVE CLASS TODAY.

# SAMPLE SOLUTION:
import turtle

zz_turtle = turtle.Turtle()
zz_turtle.shape('turtle')
zz_turtle.pencolor('green')
zz_turtle.pensize(5)

for x in range(10):  # From 1 through 20
    if x % 2 == 0:  # if the number is even ... "zig"
        zz_turtle.forward(35)
        zz_turtle.right(45)
    else:  # if the number is odd ... "zag"
        zz_turtle.forward(35)
        zz_turtle.left(45)

turtle.done()  # End
# Drawing onto the turtle canvas is complete, ready to close.