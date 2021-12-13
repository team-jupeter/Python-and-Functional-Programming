# 4.6 Variables and parameters are local
# lifetime
def final_amount(p, r, n, t):
    a = p * (1 + r/n) ** (n*t)
    return a

# print(a) # error
