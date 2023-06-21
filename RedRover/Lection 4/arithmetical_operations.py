import math

def addition(*num):
    res = 0
    for n in num:
        res += n
    print("Addition result: ", res)


def subtraction(*num):
    res = 0
    for n in num:
        res = res + n
    print("Subtraction result: ", str(0 - res))


def multiplication(*num):
    res = 1
    for n in num:
        res = res * n
    print("Multiplication result: ", res)


def dividing(*num):
    res = 1
    for n in num:
        res = res / n
    print("Dividing result: ", res)
