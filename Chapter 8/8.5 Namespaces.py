# # module1.py

# question = "What is the meaning of Life, the Universe, and Everything?"
# answer = 42

# # module2.py

# question = "What is your quest?"
# answer = "To seek the holy grail."

# import module1
# import module2

# print(module1.question)
# print(module2.question)
# print(module1.answer)
# print(module2.answer)

def f():
    n = 7
    print("printing n inside of f:", n)

def g():
    n = 42
    print("printing n inside of g:", n)

n = 11
print(f"printing n before calling f: {n}")
f()
print(f"printing n after calling f: {n}")
g()
print(f"printing n after calling g: {n}")