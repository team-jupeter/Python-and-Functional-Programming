# 5.1.5 Traversal and the for loop
word="Banana"
prefixes = "JKLMNOPQ"
suffix = "ack"

ix = 0
while ix < len(word):
    letter = word[ix]
    print(letter)
    ix += 1

for letter in word:
    print(letter)

for p in prefixes:
    print(p + suffix)

##### Functional
# [print(i) for i in word]
# [print(i+suffix) for i in prefixes]


