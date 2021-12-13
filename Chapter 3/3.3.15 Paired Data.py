# 3.3.15 Paired Data
celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]
print(celebs)
print(len(celebs)) # 3

for name, year in celebs: # decomposition, destructuring
    if year < 1980:
        print(name)

# Functional
x, y = [1, 2]
print(x)
print(y)


a, b = (3, 4)
print(a)
print(b)