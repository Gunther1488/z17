
x = int(input('Введите число гостей: '))

if x > 50:
    print('Ресторан')
else:
        if x >= 20 and x <= 50:
            print('Кафе')
        else:
            if x < 20:print('Дом')