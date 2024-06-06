## Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8  ## new ways for conditionals

if day == "Wednesday":
    price = price - 2
    ## price -= 2  same line up above

print("Ticket price for u is $",price)