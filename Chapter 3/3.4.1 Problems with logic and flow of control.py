# 3.4.1 Problems with logic and flow of control
numbers = [10, 5, 24, 8, 6]

# does the list have any odd numbers?
# Buggy version
for number in numbers:
    if number % 2 == 1:
        print(True)
        break
    else:
        print(False)
        break

for number in numbers:
    if number % 2 == 1:
        print(True)
        break
    print(False)

# Corrected version
for number in numbers:
    if number % 2 == 1:
        print(True)
        break
else:
    print(False)

# Verbose
count = 0
for number in numbers:
    if number % 2 == 1:
        count += 1 # Count the odd numbers
if count > 0:
    print(True)
else:
    print(False)

# Updated
numbers = [10, 5, 24, 8, 6]

count = 0
for number in numbers:
    if number % 2 == 1:
        count += 1 # Count the odd numbers
print(count > 0) # Aha! a programmer who understands that Boolean
                 # expressions are not just used in if statements!

# Updated
numbers = [10, 5, 24, 8, 6]
count = 0
for number in numbers:
    count += number % 2 == 1
print(count > 0)


# count += number % 2 == 1
# Order of Evaluation
# 1
# number % 2
# ==
# +
# =

# List Comprehension
numbers = [10, 5, 24, 8, 6]
a = [number for number in numbers if number % 2 == 1]
print(len(a) > 0)

# Functional
numbers = [10, 5, 24, 8, 6]
print(any(number % 2 == 1 for number in numbers))

