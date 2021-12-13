# 4.17.1 Modifiers vs Pure Functions
#  side effects
def double_stuff(values):
    """ Return a new list which contains
    doubles of the elements in the list values.
    """
    new_list = []
    for value in values:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list


things = [2, 5, 9]
more_things = double_stuff(things)
print(things)
print(more_things)

things = [2, 5, 9]
things = double_stuff(things)
print(things)

def double_stuff(values):
    """ Double the elements of values in-place. """
    for index, value in enumerate(values):
        values[index] = 2 * value

things = [2, 5, 9]
more_things = double_stuff(things)
print(things)
print(more_things)
