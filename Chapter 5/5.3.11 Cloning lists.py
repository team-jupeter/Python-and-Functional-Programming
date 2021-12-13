a = [1, 2, 3]
b = a[:]
b # [1, 2, 3]

print(id(a))
print(id(b))

b[0] = 5
a # [1, 2, 3]