# Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

family_1 = input("Enter F1 members: ").split(",")
family_2 = input("Enter F2 members: ").split(",")

if len(family_1) == len(family_2):
    print("Equal")
elif len(family_1) > len(family_2):
    print(family_1)
else:
    print(family_2)