# 5.3.8 List deletion
a = ["one", "two", "three"]
del a[1]
a # ['one', 'three']

a_list = ["a", "b", "c", "d", "e", "f"]
del a_list[1:5]
a_list # ['a', 'f']

##### Functional
# Don't mutate or delete items in a list
a = ["a", "b", "c", "d", "e", "f"]
b = [a[0]] + a[5:]
print(b) # ['a', 'f']
print(a) # ["a", "b", "c", "d", "e", "f"]