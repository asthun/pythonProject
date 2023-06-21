# Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
values = list(my_dictionary.values())
i = 0
list_sum = 0
while i < len(values):
    if isinstance(values[i], int):
        list_sum += values[i]
        i += 1
print(list_sum)