# List is mutable
my_list = [2, 4, 5, 3, 6, 1]
my_list[0] = 9
my_list # [9, 4, 5, 3, 6, 1]

# Tuple is immutable
my_tuple = (2, 5, 3, 1)
my_tuple[0] = 9
# Traceback (most recent call last):
# File "<interactive input>", line 2, in <module>
# TypeError: 'tuple' object does not support item assignment

# Aliasing
list_one = [1, 2, 3, 4, 6]
list_two = list_one
list_two[-1] = 5
list_one # [1, 2, 3, 4, 5]

list_one = [1, 2, 3, 4, 6]
list_two = list_one
id(list_one) == id(list_two) # True

list_one = [1, 2, 3, 4, 6]
list_two = list_one[:]
id(list_one) == id(list_two) # False
list_two[-1] = 5
list_two # [1, 2, 3, 4, 5]
list_one # [1, 2, 3, 4, 6]