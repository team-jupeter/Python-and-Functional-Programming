# 4.10 Return values
biggest = max(3, 7, 2, 5)
x = abs(3 - 11) + 10

def area(radius):
    b = 3.14159 * radius**2
    return b

def area_2(radius):
    return 3.14159 * radius * radius

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def absolute_value_2(x):
    if x < 0:
        return -x
    return x

def bad_absolute_value(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

print(bad_absolute_value(0))

def find_first_2_letter_word(words):
    for word in words:
        if len(word) == 2:
            return word
    return ""

my_list = ["This", "is", "a", "dead", "parrot"]

find_first_2_letter_word(my_list)
find_first_2_letter_word(["I", "like", "cheese"])


# ######## Be functional
# my_list = ["This", "is", "a", "dead", "or", "live", "parrot"]
# #####
# # matched_words = [i for i in my_list if len(i) == 2]
# # print(matched_words)

# #####
# for word in my_list:
#     match len(word):
#         case 2:
#             print(word)
#             break
# else:
#     print("No matching words")

# lst = ["This", "is", "a", "dead", "or", "live", "parrot"]

# some_word = [x for x in lst if len(x) == 2] # ["is", "or"]

# some_word = any(len(x) == 2 for x in lst) # True

# some_word = filter(lambda x: len(x) == 2, lst)[0]
# print(some_word)

# some_word = filter(lambda x: len(x) == 2, lst)[:-1]

# some_word  = next(x for x in lst if len(x) == 2) # is

# gen = (x for x in lst if len(x) == 2)
# print(next(gen, 'not_found'))

# print([x for x in gen])

#######
# lst = [i for i in range(1, 6)]

# n = next((x for x in lst if x % 10 == 0), None)
# if n is None:
#     print('Not found')
# print(n)

# find = lambda fun, lst: next((x for x in lst if fun(x)), None)
# find(lambda x: x % 10 == 0, lst)
# find(lambda x: x % 5 == 0, lst)


# findall = lambda fun, lst: [x for x in lst if fun(x)]
# result = findall(lambda x: x % 5 == 0, lst)
# print(result)