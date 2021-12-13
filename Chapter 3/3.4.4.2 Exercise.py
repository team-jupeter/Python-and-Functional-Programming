start_day = int(input("Input starting day number: "))
stay_days = int(input("Onput the length of your stay: "))

match (start_day + stay_days) // 6:
    case 0: print("Returning Sunday")
    case 1: print("Returning Monday")
    case 2: print("Returning Tuesday")
    case 3: print("Returning Wednesday")
    case 4: print("Returning Thursday")
    case 5: print("Returning Firday")
    case 6: print("Returning Saturday")


