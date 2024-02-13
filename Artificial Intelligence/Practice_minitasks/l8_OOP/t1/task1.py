class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Employee(Person):
    def __init__(self, name, age, gender, employee_id, position):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Major: {self.major}")


# Create instances and display information
employee = Employee("John Doe", 30, "Male", 1001, "Manager")
student = Student("Jane Smith", 20, "Female", 2023001, "Computer Science")

print("\nEmployee Information:")
employee.display_info()

print("\nStudent Information:")
student.display_info()
