# Code 1 - Sum
def recursive_sum(nested_number_list):
    """Returns the total sum of all elements in nested_number_list"""
    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += recursive_sum(element)
        else:
            total += element
    return total

# Code 2 - Nested List
def recursive_sum(nested_number_list):
    """Returns the total sum of all elements in nested_number_list"""
    if len(nested_number_list) == 0:
        return 0
    #Assign the first element of nested_number_list to head, and the rest to tail.
    head, *tail = nested_number_list
    if isinstance(head, list): # If head is a list....
        return recursive_sum(head) + recursive_sum(tail)
    else:
        return head + recursive_sum(tail)

# Code 3 - Max in Nested List
def recursive_max(nested_list):
    """
    Find the maximum in a recursive structure of lists
    within other lists.
    Precondition: No lists or sublists are empty.
    """
    largest = None
    first_time = True
    for element in nested_list:
        if type(element) is list:
            value = recursive_max(element)
        else:
            value = element

        if first_time or value > largest:
            largest = value
            first_time = False

    return largest

# Code 4 = Infinite Loop
def recursion_depth(number):
    print(f"{number}", end="")
    recursion_depth(number + 1)

recursion_depth(0)

##### Functional
# Code 1 - Sum
my_list = range(10000)
sum(lambda acc, x : x + acc, my_list, 0)

# Code 2 - - Nested List
from functools import reduce
regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [item for sublist in regular_list for item in sublist]

sum = reduce(lambda acc, x : x + acc, flat_list, 0)
print(sum)

# Code 3 - Max in Nested List
print(reduce(max, flat_list))

# OR
print(reduce(lambda x, y: x if x > y else y, flat_list))


