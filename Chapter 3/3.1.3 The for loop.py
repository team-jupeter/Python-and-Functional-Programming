##### For Loop = OOP
for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
    invite = "Hi " + friend + ". Please come to my party!"
    print(invite)

#### List comprehension
## NameError: name 'friend' is not defined
# invite = "Hi " + friend + ". Please come to my party!"
# friends = ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]

# [ print(invite) for friend in friends]

### New List comprehension = (OOP + FP)/2
friends = ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]
[print("Hi " + friend + ". Please come to my party!") for friend in friends]
[print(f"Hi {friend} Please come to my party!") for friend in friends]

#### Functional = Haskell
friends = ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]
a = map(lambda x : print(f"Hi {x} Please come to my party!"), friends)
print(a)

any(map(lambda x : print(f"Hi {x} Please come to my party!"), friends))