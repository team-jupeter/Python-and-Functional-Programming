opposites = {"up": "down", "right": "wrong", "yes": "no"}
alias = opposites
copy = opposites.copy() # Shallow copy

alias["right"] = "left"
opposites["right"] # 'left'

copy["right"] = "privilege"
opposites["right"] # 'left'