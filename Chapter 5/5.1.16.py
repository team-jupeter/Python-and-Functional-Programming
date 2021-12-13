# 5.1.16 The string format method
phrase = "His name is {0}!".format("Arthur")
print(phrase)
name = "Alice"
age = 10
phrase = "I am {1} and I am {0} years old.".format(age, name)
print(phrase)
phrase = "I am {0} and I am {1} years old.".format(age, name)
print(phrase)

x = 4
y = 5
phrase = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, x, y, x * y)
print(phrase)

phrase = f"2**10 = {2**10} and {x} * {y} = {x * y:f}"
print(phrase)