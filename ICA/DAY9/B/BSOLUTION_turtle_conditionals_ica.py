# *** THIS ICA IS FOR SECTION 002 CS 1112 2:00-3:15 **
# *** IF YOU ARE NOT IN THIS CLASS MAKE SURE TO NAVIGATE TO THE CORRECT FILE ***

# CS 1112
# Learning Python (Python version: 3)
# Module 2: Conditionals ACTIVITY

'''
ACTIVITY:
Use conditionals along with turtle functions to create a small program
that does the following:

1) Prompt (ask) the user to select one of four options:
  What would you like the turtle to draw? (Or select 4 to exit)
        1) Circle
        2) Hexagon
        3) Octagon
        4) EXIT

  (Note: if the user selects 4, the program ends, and nothing is drawn to the screen.
  You can output a "goodbye" message to the screen if you wish, e.g., "Exiting program!")

2) Use if-statements and conditionals in your code to draw one of the diagrams
   (options 1, 2, or 3) or exit (option 4)

3) Once a selection is made and after the drawing is complete, if applicable, then end the program.
'''

# SAMPLE SOLUTION:
import turtle

katarina = turtle.Turtle()
katarina.shape('turtle')
katarina.pencolor('green')
katarina.pensize(4)

print("\t** What would you like the turtle to draw? (Or select 4 to exit)")
print("\t\t1) Circle")
print("\t\t2) Triangle")
print("\t\t3) Octagon")
print("\t\t4) EXIT")
choice = int(input("Enter your answer here: "))

if choice == 1:
    katarina.circle(50)  # Item 1 selected: draw a circle
if choice == 2:
    for i in range(6):  # Item 2 selected: draw a Hexagon
        angle = 360 / 3
        katarina.forward(100)
        katarina.left(angle)
if choice == 3:  # Item 3 selected: draw an Octagon
    for x in range(8):
        angle = 360 / 8
        katarina.forward(100)
        katarina.left(angle)
if choice == 4:  # Item 4 selected: exit the program and print a message
    print("Exiting program...")

print("You may now close the turtle window!")


turtle.done()