# 4.21 String handling

s = "def some_function_name(x, y):" # Get the next line from somewhere
if s.find("some") >= 0: print(s.find("some"))
if "some" in s: print("There is 'some' in s") # Also works, nice-to-know sugar coating!

def_pos = s.find("def ") # Look for "def " in the line
if def_pos == 0: # If it occurs at the left margin
    op_index = s.find("(") # Find the index of the open parenthesis
    fnname = s[4:op_index] # Slice out the function name
    print(fnname) # ... and work with it.