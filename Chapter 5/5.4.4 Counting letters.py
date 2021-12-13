letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

letter_counts # {'M': 1, 's': 4, 'p': 2, 'i': 4}

letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items) # [('M', 1), ('i', 4), ('p', 2), ('s', 4)]

# ##### Functional
# from functools import reduce

# a = reduce(lambda d, current: d.update({current : d.get(current, 0) + 1}) or d, "Mississippi", {})
# print(a)


