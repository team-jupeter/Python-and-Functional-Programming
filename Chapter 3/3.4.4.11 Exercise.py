### 1. Write a program to count how many odd numbers are in a list.
my_list = [1, 2, 3, 4, 5, -6, -7]
count = 0
for _ in my_list:
    if _ % 2 == 0:
        count += 1
print(count)

# Functional
my_list = [1, 2, 3, 4, 5, -6, -7]
odd_num = len(list(filter(lambda x : x % 2 == 0, my_list)))
print(odd_num) # 3

print(filter(lambda x : x % 2 == 0, my_list))
print(list(filter(lambda x : x % 2 == 0, my_list)))

# filter().list().len()
# filter()
    # |> list()
    # |> len()

### 2. Sum up all the even numbers in a list.
sum_even = 0
for _ in my_list:
    if _ % 2 == 0:
        sum_even += _
print(sum_even)

# Functional
print(sum(my_list))

### 3. Sum up all the negative numbers in a list.
sum_negative = 0
for _ in my_list:
    if _ < 0:
        sum_negative += _
print(sum_negative)

# Functional
print(sum(list(filter(lambda _ : _ < 0, my_list))))

### 4. Count how many words in a list have length 5.
word_list = ["abc", "abcde", "a", "ab", "peter"]

count = 0
for _ in word_list:
    if len(_) == 5:
        count += 1
print(count)

# Functional
odd_num = len(list(filter(lambda _ : len(_) == 5, word_list)))

### 5. Sum all the elements in a list up to but not including
# the first even number. (What if there is no even number?)
my_list = [1, 2, 3, 4, 5, -6, -7]

total = 0
num_to_exclude = 0
for _ in my_list:
    if _ % 2 == 0:
        num_to_exclude = _
        break

for _ in my_list:
    if _ != num_to_exclude:
        total += _

print(total)

# Functional
my_list = [1, 2, 3, 4, 5, -6, -7]
first_even = next(filter(lambda x:x%2==0, my_list))
list_sum = sum([x for x in my_list if x != first_even])
print(list_sum) # 0


# print(first_even) # 2
# list_num = list(filter(lambda x:x%2==0, my_list))
# print(list_num) # []



# Another functional
my_list = [1, 2, 3, 4, 5, -6, -7]
first_even = next(x for x in my_list if x%2==0)
list_sum = sum([x for x in my_list if x != first_even])
print(list_sum) # 0

### 6. Count how many words occur in a list up to and including the first occurrence of
# the word "sam". (What if "sam" does not occur?)
no_sams = ["jam", "ham"]
sams = ["samsam", "sam", "my_sam", "no_sam", "Team", "Jupeter"]

num_of_sams = 0
for _ in sams:
    if "sam" in _:
        num_of_sams += 1
print(num_of_sams) # 4

num_of_sams = 0
for _ in no_sams:
    if "sam" in _:
        num_of_sams += 1
print(num_of_sams) # 0

# Funcional
from functools import reduce
sams = ["samsam", "sam", "my_sam", "no_sam)"]
no_sams = ["jam", "ham"]

num_of_sams = lambda words : reduce(lambda acc, x : acc + 1 if "sam" in x else acc, words, 0)
print(num_of_sams(sams))
print(num_of_sams(no_sams))

# Why functional is better => no variable.

### 7. Add a print function to Newton's sqrt algorithm that prints out better
# each time it is calculated. Call your modified program with 25 as an argument
# and record the results.
n = 25
threshold = 0.001
approximation = n/2 # Start with some or other guess at the answer
while True:
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better

# Funcional, but not recommended yet.
n = 25
threshold = 0.001
approximation = n/2 # Start with some or other guess at the answer

better = lambda x : (x + n/x)/2 \
            if abs(x - (x + n/x)/2) < threshold \
            else better((x + n/x)/2) # Recursion

print(better(14))

# Recursion Example
fact = lambda x: 1 if x == 0 else x * fact(x-1)
print(fact(25)) # 25 * 24 * 23 * ... * 1

### 8. Write a program that prints out the first n triangular numbers.
# A call to with n = 5 would produce the following output:
def tri_num(n: int, m: int = 0):
    if n == 0:
        print(m)
    else:
        m += n
        tri_num(n-1, m) # Recursion

print(tri_num(5))

# Functional 1
tri_num = lambda n : sum(range(n+1))
print(tri_num(15)) # 15 + 14 + ... + 1


# Functional 2
tri_num = lambda x: 0 if x == 0 else x + tri_num(x-1)
print(tri_num(15)) # 15 + 14 + ... + 1


### 9. Write a program which prints True when n is a prime number and False otherwise.
# Program to check if a number is prime or not.
n = 13
for x in range(2, n // 2): # How to find out whether it is prime number
    if n%x == 0:
        print(False)
        break
else: print(True)

# Functional
n = 12 # [2, 3, 4, 5, 6]
result = next(filter(lambda _:  n%_ == 0, range(2, n//2)), None)
print(result == None)

### 10. Revisit the drunk pirate problem. This time, the drunk pirate makes a turn,
# and then takes some steps forward, and repeats this. Our social science student now
# records pairs of data: the angle of each turn, and the number of steps taken after
# the turn. Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)].
# Use a turtle to draw the path taken by our drunk friend.
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.pendown()

path =  [(160, 20), (-43, 10), (270, 8), (-43, 12)]
for _ in path:
    tess.left(_[0])
    tess.forward(_[1])

window.mainloop()

##### 11. Draw a house
import turtle
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.pendown()

path =  [(140, 90), (100, 45), (100, 90), (100, 45), (100, 45)]
for _ in path:
    tess.forward(_[0])
    tess.left(_[1])

window.mainloop()

### 12. the digit counting program
def digit_counter(n: int, count: int = 0):
    if isinstance(n, int): # 343523534
        if n > 0:
            n = n // 10
            count += 1
            digit_counter(n, count) # Recursion
        elif n < 0:
            digit_counter(abs(n))
        else:
            print(count)

digit_counter(324245)
digit_counter(-324245)

# Functional
digit_counter = lambda x, count=1 : print(count) \
                    if abs(x) // 10 == 0 else digit_counter(abs(x) // 10, count+1)

digit_counter(34353)
digit_counter(-34353)


# 435254236534 => 6
### 13. Write a program that counts the number of even digits in n.
def even_digit_counter(n: int):
    # -1234 => 1234 => '1234' => ['1', '2', '3', '4']
    num_list = [char for char in str(abs(n))]
    count = 0
    # print(num_list)
    for _ in num_list:
        if int(_) % 2 == 0:
            count += 1
    print(count)

even_digit_counter(12433)
even_digit_counter(-12433)

# print(-2//10) # -1

# Functional 1
from functools import reduce
n = -234245453
num_list = [char for char in str(abs(n))]
reduce(lambda acc, x : acc + 1 if int(x) % 2 == 0 else acc, num_list, 0)

# functional 2
from functools import reduce
even_digits = lambda n : reduce(lambda acc, x : acc + 1 if int(x) % 2 == 0 \
                    else acc, [char for char in str(abs(n))], 0)

print(even_digits(-345345634645546))

### 14. Write a program that computes the sum of the squares of the numbers in the list numbers. For
# example a call with, numbers = [2, 3, 4] should print 4+9+16 which is 29.
numbers = [2, 3, 4]
square_total = 0
for _ in numbers:
    square_total += _**2

print(square_total)

# Functional
square_total = lambda n : reduce(lambda acc, x : acc + x**2, n, 0)

print(square_total([3, 5, 7, 8]))