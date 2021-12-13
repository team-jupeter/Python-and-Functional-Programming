inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory) # {'pears': 217, 'apples': 430, 'oranges': 525, 'bananas': 312}

del inventory["bananas"]
print(inventory) # {'apples': 430, 'oranges': 525, 'pears': 217}

inventory["bananas"] = 0
print(inventory) # {'pears': 217, 'apples': 430, 'oranges': 525, 'bananas': 0}

inventory["bananas"] += 200
print(inventory) # {'pears': 0, 'apples': 430, 'oranges': 525, 'bananas': 512}

len(inventory)

# ###### Functional
# inventory1 = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

# # del inventory["bananas"]
# inventory2 = dict(inventory1)
# del inventory2["bananas"]

# # inventory["bananas"] = 0
# inventory3 = dict(inventory1)
# inventory3["bananas"] = 0

# # inventory["bananas"] += 200
# inventory4 = dict(inventory1)
# inventory4["bananas"] += 200

# print(inventory1)
# print(inventory2)
# print(inventory3)
# print(inventory4)


