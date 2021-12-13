# 5.1.7 String comparison
word = input('Input your word, please.')

if word == "banana":
    print("Yes, we have no bananas!")

if word < "banana":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no bananas!")