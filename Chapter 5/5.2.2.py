# 5.2.2 Tuple assignment
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress",
    "Atlanta, Georgia")
(name, surname, year_born, movie, year_movie, profession, birthplace) = julia

bob = ("Bob", 19, "CS") # tuple packing
(name, age, studies) = bob # tuple unpacking
name # 'Bob'
age # 19
studies # 'CS'

# Swap 1
temp = a
a = b
b = temp

# Swap 2
(a, b) = (b, a)

# Error
(one, two, three, four) = (1, 2, 3) # ValueError: need more than 3 values to unpack


