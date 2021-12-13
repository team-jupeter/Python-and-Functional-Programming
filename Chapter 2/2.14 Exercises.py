# All work and no play makes Jack a dull boy
all = "All "
work = "work "

print(all + work)

# Calculate using parenthesis
6 * 1 - 2 # 4
6 * (1 - 2) # -6

# "name" is better than "variable"
bruce = 3
print(bruce + 4 )

# Annual compound/complex interest
t = int(input("What is the number of years?"))
n = int(input("How many times to compound interest per year"))
r = float(input("Interest rate"))
p = float(input("principal"))
a = p*(1+r/n)**(n*t)

#
print(5 % 2) # 1
print(9 % 5) # 4
print(15 % 12) # 3
print(12 % 15) # 12
print(6 % 6) # 0
print(0 % 7) # 0
print(7 % 0) # Error

print(2 + (51 % 24))

