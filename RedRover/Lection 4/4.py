# Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
import functools

my_list = [20, -3, 15, 2, -1, -21]

print(functools.reduce(lambda a, b: a * b, my_list))
