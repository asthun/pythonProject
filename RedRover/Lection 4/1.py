# Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
import math

def my_function(x):
  perimeter = x * 4
  square = x * x
  diagonal = x * math.sqrt(2)
  results = (perimeter, square, diagonal)
  print(results)

my_function(2)