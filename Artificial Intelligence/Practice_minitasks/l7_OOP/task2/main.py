import ClassCircle


def main():
    radius = float(input("Enter the radius of the circle: "))

    my_circle = ClassCircle.Circle(radius)

    print("Area of the Circle is :", my_circle.get_area())
    print("Diameter of the Circle is :", my_circle.get_diameter())
    print("Circumference of the Circle is :", my_circle.get_circumference())


main()
