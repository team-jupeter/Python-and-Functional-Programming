import turtle
window = turtle.Screen() # Set up the window and its attributes
window.bgcolor("lightgreen")
window.title("Tess & Alex")

tess = turtle.Turtle() # Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

# tess.forward(80) # Make tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120) # Complete the triangle

# for _ in [0,1,2]:
#     tess.forward(80) # Make tess draw equilateral triangle
#     tess.left(120)

for _ in range(3): # [0, 1, 2]
    tess.forward(80) # Make tess draw equilateral triangle
    tess.left(120)

tess.right(180) # Turn tess around
tess.forward(80) # Move her away from the origin

alex = turtle.Turtle() # Create alex
# alex.forward(50) # Make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

for _ in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)

# window.mainloop()

# for i in range(4):
# # Executes the body with i = 0, then 1, then 2, then 3

# for x in range(10):
# # Sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for color in ["yellow", "red", "purple", "blue"]:
    alex.color(color)
    alex.forward(50)
    for _ in range(4):
        alex.forward(50)
        alex.left(90)
window.mainloop()

# # Assign a list to a variable
# colors = ["yellow", "red", "purple", "blue"]
# for color in colors:
#     alex.color(color)
#     alex.forward(50)
#     alex.left(90)



