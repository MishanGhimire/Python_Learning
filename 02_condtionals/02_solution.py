age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8  ## new ways for conditionals

if day == "Wednesday":
    price = price - 2
    ## price -= 2  same line up above

print("Ticket price for u is $",price)