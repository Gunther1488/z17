x = input()
length = len(x)
z = int(length / 2)
if length % 2 == 0:
    print(x[(z) - 1:(z)])
else:
    if length % 2 != 0 and x != ([z]):
        print(x[(z)], (x[1: -1]))