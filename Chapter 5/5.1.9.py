# 5.1.9 The in and not in operators
"p" in "apple" # True
"i" in "apple" # False

"ap" in "apple" # True
"pa" in "apple" # False

"a" in "a" # True
"apple" in "apple" # True
"" in "a" # True
"" in "apple" # True

"x" not in "apple" # True

def remove_vowels(phrase):
    vowels = "aeiou"
    string_sans_vowels = ""
    for letter in phrase:
        if letter.lower() not in vowels:
            string_sans_vowels += letter
    return string_sans_vowels

# ###### Functional
# ###
# def remove_vowels(phrase):
#     return [i for i in phrase if i not in "aeiou"]

# result = remove_vowels("Team Jupeter")
# print(result)

# ###
# result = list(filter(lambda x: (x not in "aeiou"), "Team Jupeter"))
# print(result)