mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
mylist # [5, 27, 3, 12]

mylist.insert(1, 12) # Insert 12 at pos 1, shift other items up
mylist # [5, 12, 27, 3, 12]
mylist.count(12) # How many times is 12 in mylist? 2
mylist.extend([5, 9, 5, 11])
mylist # [5, 12, 27, 3, 12, 5, 9, 5, 11])
mylist.index(9) # Find index of first 9 in mylist - 6
mylist.reverse()
mylist # [11, 5, 9, 5, 12, 3, 27, 12, 5]
mylist.sort()
mylist # [3, 5, 5, 5, 9, 11, 12, 12, 27]
mylist.remove(12) # Remove the first 12 in the list
mylist # [3, 5, 5, 5, 9, 11, 12, 27]


###### Functional
# Notice that no list is to be changed.
a = []
b = a + [5]
c = b + [27]
d = c + [3]
e = d + [12]

f = [e[0]] + [12] + e[1:] # a.insert(1, 12)
f.count(12) # How many times is 12 in a? 2
g = f + [5, 9, 5, 11]
g.index(9) # Find index of first 9 in a - 6
h = reversed(g) #a.reverse()
i = sorted(h)
# j = i - [12] # Remove the first 12 in the list

print(i)

print(h)
print(list(h))


