a = [1, 2, 3]
b = a
a is b # True

print(id(a))
print(id(b))

b[0] = 5
a # [5, 2, 3]

