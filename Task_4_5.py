# first solution
a1 = 1
a2 = 1
a = int(input())
print(a1, a2)
while a > 2:
    a1, a2 = a2, a1 + a2
    print(a2)
    a -= 1

# second solution
a1 = 1
a2 = 1
a = int(input())
print(a1, a2)
for i in range(2, a):
    a1, a2 = a2, a1 + a2
    print(a2)
