number = 3

for i in range(1, 11):
    if i == 5:
        continue  ## skips 5th iteration
    print(number, 'x', i, '=', number * i)
