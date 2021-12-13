def function_a(n): # Do things associated with state A
    if n == 0:
        return
    print('a')
    function_b(n - 1) # Proceed to state B


def function_b(n): # Do things associated with state B
    print('b')
    function_a(n - 1) # Proceed to state A