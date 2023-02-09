import math
import turtle

# Named constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
turtlenum = 0

# Size the window.
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Calculate the diameter of the octagon so we
# can center it in the graphics window.
#                s
#        ---------------
#       / |             \
#  s   /  |              \
#     /   | x             \  s
#    /    |                \
#   |------                 |
#   |   x                   |
#   |                       |
#   To get the diameter:
s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

# Initialize the turtle.


# Move the turtle to the starting point.



# Draw the octagon.
turtle.color('red')
style = ('arial', 30, 'bold')
while turtlenum <= 7:
    turtle.forward(100)
    turtle.right(45)
    turtlenum = turtlenum + 1

# Display 'STOP'
turtle.right(90)
turtle.up()
turtle.forward(x * 2)
turtle.write("STOP",font=style)


