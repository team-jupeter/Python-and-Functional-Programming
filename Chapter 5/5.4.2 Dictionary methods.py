english_spanish = {}
english_spanish["one"] = "uno"
english_spanish["two"] = "dos"

print(english_spanish) # {"two": "dos", "one": "uno"}

for key in english_spanish.keys(): # The order of the k's is not defined
    print("Got key", key, "which maps to value", english_spanish[key])

keys = list(english_spanish.keys())
print(keys)

#  omit the keys method
for key in english_spanish:
    print("Got key", key)

list(english_spanish.values()) # ['tres', 'dos', 'uno']
list(english_spanish.items()) # [('three', 'tres'), ('two', 'dos'), ('one', 'uno')]

for (key,value) in english_spanish.items():
    print("Got",key,"that maps to",value)

"one" in english_spanish # True
"two" in english_spanish # False
"tres" in english_spanish # False. Note that 'in' tests keys, not values.