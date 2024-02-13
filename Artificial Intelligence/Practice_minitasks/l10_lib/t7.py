import math


def calculate_circle_area(radius):
    area = (math.pi * (radius**2))
    return area


Radius = int(input('Enter the radius to calculate the circle area: '))
area = calculate_circle_area(Radius)
print(f"The area of a circle with radius {Radius} is: {area}")
