print(type("Hello, World!")) # <class 'str'>
print(type(17)) # <class 'int'>

print(type(3.2)) # <class 'float'>
print(type("17")) # <class 'str'>
print(type("3.2")) # <class 'str'>

print(type('This is a string.')) # <class 'str'>
print(type("And so is this.")) # <class 'str'>
print(type("""and this.""")) # <class 'str'>
print(type('''and even this...''')) # <class 'str'>

print('''"Oh no", she exclaimed, "Ben's bike is broken!"''') # "Oh no", she exclaimed, "Ben's bike is broken!"

message = """This message will
            span several
            lines."""

print(message)
# message2 = "This message will
#             span several
#             lines."

# print(message)

print(42000)
print(42,000)


def fun():
    print("hi")

class MyClass:
    a: int

print(id(fun))
print(id(MyClass))

a = 1
print(id(a))
print(id(1))

b = 1
print(id(b))
