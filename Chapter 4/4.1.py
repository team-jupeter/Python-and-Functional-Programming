# 4.1 Functions

# def <NAME>( <PARAMETERS> ):
#     <STATEMENTS>

# import turtle

# # Comments at the start of a function are Docstrings for documentation
# def draw_square(animal, size):
#     """
#     Make animal draw a square with sides of length size.
#     """
#     for _ in range(4):
#         animal.forward(size)
#         animal.left(90)


#         window = turtle.Screen() # Set up the window and its attributes
#         window.bgcolor("lightgreen")
#         window.title("Alex meets a function")

# alex = turtle.Turtle() # Create alex
# draw_square(alex, 50) # Call the function to draw the square

# window.mainloop()

import turtle

def draw_multicolor_square(animal, size):
    """Make animal draw a multi-color square of given size."""
    for color in ["red", "purple", "hotpink", "blue"]:
        animal.color(color)
        animal.forward(size)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")

tess = turtle.Turtle() # Create tess and set some attributes
tess.pensize(3)

size = 20 # Size of the smallest square

for _ in range(15):
    draw_multicolor_square(tess, size)
    size += 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

window.mainloop()