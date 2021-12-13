def draw_rectangle(animal, width, height):
    """Get animal to draw a rectangle of given width and height."""
    for _ in range(2):
        animal.forward(width)
        animal.left(90)
        animal.forward(height)
        animal.left(90)

def draw_square(animal, size): # A new version of draw_square
    draw_rectangle(animal, size, size)

