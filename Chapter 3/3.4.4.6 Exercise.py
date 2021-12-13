# Mark Grade
# >= 75 First
# [70-75) Upper Second
# [60-70) Second
# [50-60) Third
# [45-50) F1 Supp
# [40-45) F2
# < 40 F3

mark = input('Enter exam mark: ')
try:
    fmark = float(mark) # 34e
except:
    print('Exam mark must be a number.')
    quit()

grade = ''

# "match case" is possible but not so clean.
if fmark >= 75:
    grade = 'First'
elif 70 <= fmark < 75:
    grade = 'Upper Second'
elif 60 <= fmark <70:
    grade = 'Second'
elif 50 <= fmark < 60:
    grade = 'Third'
elif 45 <= fmark < 50:
    grade = 'F1 Supp'
elif 40 <= fmark < 45:
    grade = 'F2'
else:
    grade = 'F3'

print(grade)

numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]
