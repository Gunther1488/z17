from random import randint

m=int(input())
n=int(input())

print(" ")
a = [[randint(1,20) for j in range(n)] for i in range(m)]
for i in range(m):
    print(a[i],max(a[i]))
for i in range(n):
    x=[x[i] for x in a]
    print((x), end=" ")