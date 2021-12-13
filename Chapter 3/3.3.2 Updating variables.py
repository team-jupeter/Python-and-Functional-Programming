# 3.3.2 Updating variables

# n = 5
# print(id(n))
# n = 3 * n + 1
# print(id(n))

# m = 5
# print(id(m))
# print(id(n))

# mutable
runs_scored = 0
runs_scored = runs_scored + 1
runs_scored = runs_scored + 1
runs_scored += 1
print(runs_scored) # 3