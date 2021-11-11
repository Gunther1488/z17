x = input()
sum = 0
mult = 1
for digit in x:
    sum += int(digit)
    mult *= int(digit)
print(sum, mult)