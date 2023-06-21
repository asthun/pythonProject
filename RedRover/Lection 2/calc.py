"""
Напишите программу-калькулятор, которая принимает два числа и оператор (в формате str), 
производит заданное арифметическое действие и печатает результат в формате: {num1} {operator) {num2) = {result}
"""

import operator

num1 = input("1st number: ", )
num2 = input("2d number: ", )
op = input("operator: ", )

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

print(num1 + op + num2 + ' = ' + str(ops[op](int(num1), int(num2))))