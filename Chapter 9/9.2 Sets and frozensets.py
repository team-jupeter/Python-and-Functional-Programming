my_set = set([1, 4, 2, 3, 4])
my_set # {1, 2, 3, 4}
my_set.add(13)
my_set # {1, 2, 3, 4, 13}

set1 = set([1, 2, 3])
set2 = set([4, 5, 6])
print(set1 | set2) # {1, 2, 3, 4, 5, 6}
print(set1 & set2) # set()
set2 = set([2, 3, 4, 5])
print(set1 & set2) # {2, 3}
print(set1 - set2) # {1}