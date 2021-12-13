# 2.7 Type converter functions
int(3.14) # 3
int(3.9999) # This doesn't round to the closest int! 3
int(3.0) # 3
int(-3.999) # Note that the result is closer to zero. -3
minutes = 37654
print(minutes / 60)
a = int(minutes / 60) # 10
print(int(minutes / 60))

# Expression is evaluated from left to right. and inside to outside.

int("2345") # Parse a string to produce an int. 2345
int(17) # It even works if arg is already an int. 17
int("23 bottles") # Error
float(17) # 17.0
float("123.45 a") # 123.45
str(17) # '17'
str(123.45) # '123.45'

# v(c) = func(argument)

# 2.8 Order of operations
# PEMDAS = Parenthesis, Exponentiation, Multiplication,Division, Addition, Subtraction.
2 ** 3 ** 2 # The right-most ** operator gets done first! # 512
(2 ** 3) ** 2 # Use parentheses to force the order you want! # 64

# 2.9 Operations on strings
message = "Hello, World"
# message - 1 # Error
# "Hello" / 123 # Error
# message * "Hello" # Error
# "15" + 2 # Error
print(message*2)

fruit = "banana"
baked_good = " nut bread"
print(fruit + baked_good)

# String + String, String * Int

# 2.10 Input
name = input("Please enter your name: ")

# 2.11 Composition
# Code 1
response = input("What is your radius? ") # string. '3.5'
r = float(response)
area = 3.14159 * r**2
print("The area is ", area)

# Code 2
r = float(input("What is your radius? "))
print("The area is ", 3.14159 * r**2)

# Code 3
print("The area is ", 3.14159*float(input("What is your radius?"))**2)

# 2.12 The modulus operator
q = 7 // 3 # This is integer division operator
print(q) # 2
r = 7 % 3
print(r) # 1

total_secs = int(input("How many seconds, in total?"))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, " mins=", minutes, "secs=", secs_finally_remaining)