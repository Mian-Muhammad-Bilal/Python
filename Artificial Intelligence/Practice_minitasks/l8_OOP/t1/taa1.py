class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(
            f"Displaying person data:\nName: {self.name}, Age: {self.age}, Gender: {self.gender}")


class Employee(Person):
    def __init__(self, name, age, gender, employee_id, position):
        Person.__init__(self, name, age, gender)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        Person.display_info(self)
        print(
            f"Displaying Employee data:\nEmployee ID: {self.employee_id}, Position: {self.position}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        Person.__init__(self, name, age, gender)
        self.student_id = student_id
        self.major = major

    def display_info(self):
        Person.display_info(self)
        print(
            f"Displaying student data:\nStudent ID: {self.student_id}, Major: {self.major}")


def main():
    E1 = Employee("Asif", 30, "Male", 101, "Manager")
    E1.display_info()

    S1 = Student("Javeria", 21, "Female", 2023, "Computer Science")
    S1.display_info()


if __name__ == "__main__":
    main()
