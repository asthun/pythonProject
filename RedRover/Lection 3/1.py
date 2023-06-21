# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3

my_list = ['a', 'b', [1, 2, 3], 'd']
list_to_type = my_list[2]
i = 0
while i < len(list_to_type):
    print(str(list_to_type[i]) + ", ")
    i += 1
