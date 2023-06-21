"""
Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35
	position: web developer
"""


def my_function(**employees):
    for key, value in employees.items():
        print(f"{key}: {value}")


my_function(name="John", last_name="Smith", age="35")
