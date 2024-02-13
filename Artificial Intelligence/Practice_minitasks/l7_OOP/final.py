##############TASK NO.1

import PRclass
#code:

class PayRoll:
    epr = 0.0
    no_of_hours = 0.0

    def set_hourly_rate(self, rate):
        self.epr = rate

    def set_hours_worked(self, hours):
        while hours > 60:
            print("Error!!! Hours worked limit is 60.")
            hours = float(
                input("Enter number of hours worked less than or 60: "))

        self.no_of_hours = hours

    def calculate_pay(self):
        return self.epr * self.no_of_hours

def main():
    n = int(input("Enter the number of employees: "))
    PR_list = [PRclass.PayRoll() for j in range(n)]

    for i in range(n):
        print(f"\nEnter details for Employee no.{i + 1}:")
        epr = float(input("Enter hourly pay rate: "))
        no_of_hours = float(input("Enter number of hours worked: "))
        PR_list[i].set_hourly_rate(epr)
        PR_list[i].set_hours_worked(no_of_hours)

    print("\nPayroll Results:")
    for i in range(n):
        total_pay = PR_list[i].calculate_pay()
        print(f"Total Pay of Employee no.{i + 1} is \"{total_pay}\"")

main()


#-----------------------------------------------------------------------------
##############TASK NO.2

import ClassCircle
#code:

class Circle:
    pi = 3.14159

    def __init__(self):
        self.radius = 0.0

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_area(self):
        return Circle.pi * self.radius * self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_circumference(self):
        return 2 * Circle.pi * self.radius


def main():
    radius = float(input("Enter the radius of the circle: "))

    my_circle = ClassCircle.Circle(radius)

    print("Area of the Circle is :", my_circle.get_area())
    print("Diameter of the Circle is :", my_circle.get_diameter())
    print("Circumference of the Circle is :", my_circle.get_circumference())

main()