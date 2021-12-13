# 3.3.14 The continue statement
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1: # If the number is odd
        continue # Don't process it
    print(i)
print("done")