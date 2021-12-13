import turtle
window = turtle.Screen()
tess = turtle.Turtle()

tess.pendown()

path =  [(140, 90), (100, 45), (100, 90), (100, 45), (100, 45)]
for _ in path:
    tess.forward(_[0])
    tess.left(_[1])

window.mainloop()

-34252435345