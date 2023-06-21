# Напишите программу, которая проверяет здоровье персонажа в игре.
# Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
import random

x = random.randint(-100, 100)
if x > 0:
    print(str(x) + " " + "True")
else:
    print(str(x) + " " + "False")