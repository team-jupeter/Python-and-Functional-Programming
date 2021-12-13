# 3.3.11 The break statement
# The pre-test loop — standard loop behaviour
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1: # If the number is odd
        break # ... immediately exit the loop
    print(i)
print("done")