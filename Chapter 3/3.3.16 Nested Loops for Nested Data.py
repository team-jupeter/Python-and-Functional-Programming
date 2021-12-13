# 3.3.16 Nested Loops for Nested Data
students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# Print all students with a count of their courses.
for name, subjects in students:
    # print(name, "takes", len(subjects), "courses")
    print(f"{name} takes {len(subjects)} courses")

# Count how many students are taking CompSci
counter = 0
for name, subjects in students:
    for s in subjects: # A nested loop!
        if s == "CompSci":
            counter += 1

print(f"The number of students taking CompSci is {counter}")

counter = 0
for name, subjects in students:
    if "CompSci" in subjects:
        counter += 1
print(f"The number of students taking CompSci is {counter}")

# List Comprehension returns a list which has the same number of items as input list.
a = ["CompSci" in subjects for name, subjects in students]
print(a)


