
arr = [1, 2, 3, 4, 5]
import random
a = 0
while a<19:
    arr.append(random.randint(-100,100))
    a %= 2
print(arr)

max(arr)