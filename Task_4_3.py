# first solution
a_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(a_dict.keys()) :
    a_dict[key + str(len(key))] = a_dict.pop(key)
print(a_dict)


# second solution
