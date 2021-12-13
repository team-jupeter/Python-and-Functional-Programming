# 5.1.8 Strings are immutable
greeting = "Hello, world!"
greeting[0] = 'J' # ERROR!
print(greeting)

greeting = "Hello, world!"
new_greeting = "J" + greeting[1:]
print(new_greeting)