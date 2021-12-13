import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup() # This is new. EMC, Scratch
# tess.pendown() # This is new. EMC, Scratch
distance = 20

for _ in range(30):
    tess.stamp() # Leave an impression on the canvas
    distance = distance + 3 # Increase the distance on every iteration
    tess.forward(distance) # Move tess along
    tess.right(24) # ... and turn her

window.mainloop()