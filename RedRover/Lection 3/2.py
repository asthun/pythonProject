"""
Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
   - получите сумму всех чисел,
   - распечатайте все строки, где есть буква 'a'
"""
list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
i = 0
list_sum = 0
while i < len(list_1):
    if isinstance(list_1[i], int):
        list_sum += list_1[i]
        i += 1
    elif isinstance(list_1[i], str):
        if list_1[i].find('a') != -1:
            print(list_1[i])
            i += 1
        else:
            i += 1
    else:
        i += 1
print(list_sum)