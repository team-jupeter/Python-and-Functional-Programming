def double_stuff(a_list):
    """ Return a new list which contains
    doubles of the elements in a_list.
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)

    return new_list

things = [2, 5, 9]
more_things = double_stuff(things)
things # [2, 5, 9]
more_things # [4, 10, 18]

things = [2, 5, 9]
things = double_stuff(things)
things # [4, 10, 18]

# #### Functional
# # for item
# double = lambda x: x * 2
# print(double(5))

# # for list
# double_stuff = lambda xs : map(lambda x : x * 2, xs)

# things = [2, 5, 9]
# new_things = double_stuff(things)

# print(things) # unchanged
# print(new_things)
# print(list(new_things))