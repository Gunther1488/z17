
while True:
    sign = input("Знак (+,-,*,/): ")
    if sign == "0":
        break
    if sign in "(+,-,*,/)":
        x = int(input("x = "))
        y = int(input("y = "))
        if sign == "+":
            print(x + y)
        elif sign == "-":
            print(x - y)
        elif sign == "*":
            print(x * y)
        elif sign == "/":
            if y != 0:
                print (x / y)
            else:
                if sign == 0:
                    break





