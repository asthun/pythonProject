# asterisks
"""
1.2
    1) Напишите программу, чтобы вывести:

*********
*       *
*       *
*********
"""
width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

if height >= 1:
    print(width * '*')

while height-2 > 0:
    print('*' + (width-2)*' ' + '*')
    height = height-1

if height > 1:
    print(width * '*')
