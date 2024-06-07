## Problem: Given a string, find the first non-repeated character.
input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
       print("Character is: ", char)
       break