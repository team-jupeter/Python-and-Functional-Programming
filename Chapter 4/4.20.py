# 4.20 Local variables
import turtle

tess = turtle.Turtle() # Create tess and set some attributes

size = 2
def h2():
    """ Draw the next step of a spiral on each call. """
    global size
    tess.turn(42)
    tess.forward(size)
    size += 10

for _ in range(15):
    # draw_multicolor_square(tess, size)
    size += 10 # Increase the size for next time
    tess.forward(10) # Move tess along a little
    tess.right(18) # and give her some turn

# #### Be functional
# # NO global variable
# def h2(size):
#     tess.turn(42)
#     tess.forward(size)

# for _ in range(15):
#     # draw_multicolor_square(tess, size)
#     size += 10 # Increase the size for next time
#     h2(size)


