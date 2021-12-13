a = "banana"
b = "banana"
a is b # True
print(id(a))
print(id(b))

a = [1, 2, 3]
b = [1, 2, 3]
a == b # True
a is b # False
print(id(a))
print(id(b))

