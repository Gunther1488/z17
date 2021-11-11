# first solution
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
b = i = 0
while i < n :
    b += (a[i] + 1) % 2
    i += 1
print(b)

# second solution
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
