# first solution
list = [0,1,2,3,4,5,6,7]
for a in range(len(list)):
    list[a] *= -2
print(list)

# second solution
list = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12]
i = 0
while i < len(list):
    list[i] *= -2
    i += 1
print(list)
