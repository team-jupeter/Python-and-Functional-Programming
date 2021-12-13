# Lists are mutable
fruit = ["banana", "apple", "quince"]
fruit[0] = "pear"
fruit[2] = "orange"
fruit # ['pear', 'apple', 'orange']

# my_string = "TEST"
# my_string[2] = "X"
# Traceback (most recent call last):
# File "<interactive input>", line 1, in <module>
# TypeError: 'str' object does not support item assignment

my_list = ["T", "E", "S", "T"]
my_list[2] = "X"
my_list # ['T', 'E', 'X', 'T']

a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = ["x", "y"]
a_list # ['a', 'x', 'y', 'd', 'e', 'f']

a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = []
a_list # ['a', 'd', 'e', 'f']

a_list = ["a", "d", "f"]
a_list[1:1] = ["b", "c"]
a_list # ['a', 'b', 'c', 'd', 'f']
a_list[4:4] = ["e"]
a_list # ['a', 'b', 'c', 'd', 'e', 'f']

##### Functional
# Don't Mutate a List
# Code 1
a_list = ["a", "d", "f"]
a_list[1:1] = ["b", "c"]
a_list # ['a', 'b', 'c', 'd', 'f']
a_list[4:4] = ["e"]
a_list # ['a', 'b', 'c', 'd', 'e', 'f']

# Code 2
a = ["a", "d", "f"]
b = a[0] + ["b", "c"] + a[1:]
a # ['a', 'd', 'f']
b # ['a', 'b', 'c', 'd', 'f']
c = b + ["e"]
a # ['a', 'd', 'f']
b # ['a', 'b', 'c', 'd', 'f']
c # ['a', 'b', 'c', 'd', 'e', 'f']