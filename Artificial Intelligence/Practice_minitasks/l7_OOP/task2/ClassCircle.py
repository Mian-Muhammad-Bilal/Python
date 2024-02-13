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
