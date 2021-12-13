day_num = input('Input day number: ')
# if day_num == 0:
#     print("Sunday")
# elif day_num == 1:
#     print("Monday")

# Python v3.10
# Functional = Structured Pattern Matching == Scala, Elixir
match day_num // 6: # Expression
    case 0: print("Sunday") # Statement
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Firday")
    case 6: print("Saturday")