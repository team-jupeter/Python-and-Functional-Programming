# for <VARIABLE> in <LIST>:
#     <BODY>
# Code 1
friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
for friend in friends:
        print(friend)

for number in range(20):
    if number % 3 == 0:
        print(number)

for fruit in ["banana", "apple", "quince"]:
    print("I like to eat " + fruit + "s!")

# Code 2
xs = [1, 2, 3, 4, 5]
for i in range(len(xs)):
    xs[i] = xs[i]**2

for (i, val) in enumerate(xs):
    xs[i] = val**2

xs # [1, 4, 9, 16, 25]

for (i, v) in enumerate(["banana", "apple", "pear", "lemon"]):
    print(i, v)

##### Functional
xs = [1, 2, 3, 4, 5]
xs_new = list(map(lambda i : i**2, xs))

xs # [1, 2, 3, 4, 5]
xs_new # [1, 4, 9, 16, 25]

