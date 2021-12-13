def count_a(text):
    count = 0
    for letter in text:
        if letter == "a":
            count += 1
    return(count)

print(count_a("banana"))

# #### Functional
# # 1
# result = list(filter(lambda x: (x == "a"), "banana"))
# print(len(result))

# # 2
# result = sum(i == "a" for i in "banana")
# print(result)

# # 3
# result = sum(1 for i in "banana" if i == "a")
# print(result)
