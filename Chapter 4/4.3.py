# 4.3 Flow of execution
import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

window = turtle.Screen() # Set up the window and its attributes

tess = turtle.Turtle() # Create tess and set some attributes
draw_square(tess, 50)
window.mainloop()