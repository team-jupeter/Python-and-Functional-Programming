
remind = 'Length must be a number.'
a = input('Enter length of first side of triangle (cm): ')
try: # 34.5
    fa = float(a)
except:
    print(remind)
    quit()

b = input('Enter length of second side of triangle (cm): ')
try:
    fb = float(b)
except:
    print(remind)
    quit()

hypotenuse = (fa**2 + fb**2)**0.5


