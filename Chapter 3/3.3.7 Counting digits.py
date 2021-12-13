# Counting digits
n = 3029
count = 0
while n != 0:
    count = count + 1
    n = n // 10 # floor division
print(count)

n = 2574301453
count = 0
while n > 0:
    digit = n % 10 # modular
    if digit == 0 or digit == 5:
        count = count + 1
    n = n // 10 # floor division
print(count)