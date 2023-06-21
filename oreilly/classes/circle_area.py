import math


def area(r):
    return math.pi * r**2

def circumference(r):
    return math.pi * r * 2


radius = float(input("Circle radius: "))

circle_area = area(radius)
circumference_length = circumference(radius)

print("Area: " + str(circle_area))
print("Circumference: " + str(circumference_length))