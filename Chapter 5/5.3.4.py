# 5.3.4 List membership
horsemen = ["war", "famine", "pestilence", "death"]
"pestilence" in horsemen # True
"debauchery" in horsemen # False
"debauchery" not in horsemen # True

# Nested Loops for Nested Data:
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# Count how many students are taking CompSci
counter = 0
for name, subjects in students:
    if "CompSci" in subjects:
        counter += 1
print("The number of students taking CompSci is", counter)

# ##### Functional
# result = filter(lambda student : "CompSci" in  student[1], students)

# print(list(result))
# print(len(list(result)))


