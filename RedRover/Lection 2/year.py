# Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600). Однако, если год делится без остатка
# на 400, он также считается високосным (1200, 2000)

x = int(input())
if x % 400 == 0:
    print("V")
elif x % 100 == 0 and x % 4 != 0:
    print("!=V")
elif x % 4 == 0:
    print("V")
else:
    print("!=V")