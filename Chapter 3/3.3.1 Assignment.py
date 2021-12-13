# Assignment Statement
airtime_remaining = 15
print(airtime_remaining) # 15
airtime_remaining = 7
print(airtime_remaining) # 7

# Name = Expression
a = 5
b = a # After executing this line, a and b are now equal
print(id(a))
print(id(b))

a = 3 # After executing this line, a and b are no longer equal
print(id(a))
print(id(b))
