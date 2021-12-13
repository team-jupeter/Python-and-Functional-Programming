def double_stuff(stuff_list):
    """ Overwrite each element in a_list with double its value. """
    for (index, stuff) in enumerate(stuff_list):
        stuff_list[index] = 2 * stuff

things = [2, 5, 9]
double_stuff(things)
print(things)

# ##### Functional
# # Don't mutate a list.
# things = [2, 5, 9]
# new_things = list(map(lambda i : i*2, things))

# print(things)
# print(new_things)