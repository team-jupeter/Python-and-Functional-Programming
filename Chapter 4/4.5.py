# Functions that return values
biggest = max(3, 7, 2, 5)
x = abs(3 - 11) + 10

# fruitful function vs. void function
def final_amount(p, r, n, t):
    """
    Apply the compound interest formula to p
    to produce the final amount.
    """
    a = p * (1 + r/n) ** (n*t)
    return a # This is new, and makes the function fruitful.

# now that we have the function above, let us call it.
toInvest = float(input("How much do you want to invest?"))

#  8% interest, compounded 12 times per year, for 5 years
fnl = final_amount(toInvest, 0.08, 12, 5)
print("At the end of the period you'll have", fnl)

def final_amount_v2(principal_amount, nominal_percentage_rate,
    num_times_per_year, years):
    a = principal_amount * (1 + nominal_percentage_rate /
    num_times_per_year) ** (num_times_per_year*years)
    return a

def final_amount_v3(amount, rate, compounded, years):
    a = amount * (1 + rate/compounded) ** (compounded*years)
    return a

def final_amount_v4(amount, rate, compounded, years):
    """
    The a in final_amount_v3 was a useless asignment.
    We might as well skip it.
    """
    return amount * (1 + rate/compounded) ** (compounded*years)