
remind = 'Length must be a number.'
sides = []
first_side = input('Enter length of the first side of triangle (cm): ')
try:
    sides.append(float(first_side))
except:
    print(remind)
    quit()

second_side = input('Enter length of the second side of triangle (cm): ')
try:
    sides.append(float(second_side))
except:
    print(remind)
    quit()

third_side = input('Enter length of the third side of triangle (cm): ')
try:
    sides.append(float(third_side))
except:
    print(remind)
    quit()

sides.sort()
#print('longest side is',sides[-1])
#quit()

x = sides[2]**2 # square of longest side
y = sides[0]**2 + sides[1]**2 # sum of the squares of the remaining 2 sides

threshold = 1e-7
if abs(x - y) < threshold:
    print(True)
else:
    print(False)
