# 5.1.12 Optional parameters
def find2(haystack, needle, start):
    for index,letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return -1

print(find2("banana", "a", 2) == 3)

def find(haystack, needle, start=0):
    for index,letter in enumerate(haystack[start:]):
        if letter == needle:
            return index + start
    return -1

def find(haystack, needle, start=0, end=-1):
    for index,letter in enumerate(haystack[start:end]):
        if letter == needle:
            return index + start
    return -1

# ## If we want all the indexes of "a" after start.
# ##### Functional
# phrase = "banana"

# # Slice to get a sublist
# h_slice = lambda x, start: x[start:]

# # Get all indexes of "a"
# index_a = lambda x, f, start : [k + start for k, v in enumerate(f(x, start))
#                                 if v == "a"]
# result = index_a(phrase, h_slice, 2)
# print(result)

# index_a = lambda x, f, start=0 : [k + start for k, v in enumerate(f(x, start))
#                                 if v == "a"]
# result = index_a(phrase, h_slice)
# print(result)

