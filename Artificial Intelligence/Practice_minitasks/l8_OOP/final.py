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


#================================================================

import taa1

class LivingThing:
    def __init__(self, alive):
        self.alive = alive


class Human(LivingThing):
    def __init__(self, alive, language_spoken, is_homo_sapien):
        LivingThing.__init__(self, alive)
        self.language_spoken = language_spoken
        self.is_homo_sapien = is_homo_sapien


class Superhero(taa1.Person, Human):

    def __init__(self, name, age, gender, alive, language_spoken, is_homo_sapien, superhero_name):
        taa1.Person.__init__(self, name, age, gender)
        self.name = name
        self.age = age
        self.gender = gender
        Human.__init__(self, alive, language_spoken, is_homo_sapien)
        self.superhero_name = superhero_name

    def save_the_day(self):
        print(f"{self.superhero_name} is saving the day!")

    def disply_info(self):
        print(f"Superhero Name: {self.superhero_name}")
        print(f"Alive: {'Yes' if self.alive else 'No'}")
        print(f"Language Spoken: {self.language_spoken}")
        print(f"Is Homo Sapien: {'Yes' if self.is_homo_sapien else 'No'}")


S1 = Superhero(name="Jerry", age="26", gender="male", alive=True,
               language_spoken="English", is_homo_sapien=True, superhero_name="Superman")

if __name__ == "__main__":
    S1.save_the_day()
    S1.disply_info()

#================================================================

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(
            f"Title: {self.title}, Author: {self.author}, Published in {self.publication_year}")


class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        Book.__init__(self, title, author, publication_year)
        self.file_size = file_size

    def display_details(self):
        Book.display_details(self)
        print(f"File Size: {self.file_size} MB")


class PrintedBook(Book):
    def __init__(self, title, author, publication_year, num_pages, is_hardcover):
        Book.__init__(self, title, author, publication_year)
        self.num_pages = num_pages
        self.is_hardcover = is_hardcover

    def display_details(self):
        Book.display_details(self)
        print(f"No. of Pages: {self.num_pages}")
        print(f"Is Hardcover: {'Yes' if self.is_hardcover else 'No'}")


ebooks = [
    EBook("EBook 1", "Author 1", 2022, 5.0),
    EBook("EBook 2", "Author 2", 2020, 3.5),
    EBook("EBook 3", "Author 3", 2022, 5.0),
    EBook("EBook 4", "Author 4", 2020, 3.5),
    EBook("EBook 5", "Author 5", 2022, 5.0),
    EBook("EBook 6", "Author 6", 2020, 3.5),
    EBook("EBook 7", "Author 7", 2022, 5.0),
    EBook("EBook 8", "Author 8", 2020, 3.5),
    EBook("EBook 9", "Author 9", 2022, 5.0),
    EBook("EBook 10", "Author 10", 2020, 3.5),
]

printed_books = [
    PrintedBook("Printed Book 1", "Author 1", 2019, 300, True),
    PrintedBook("Printed Book 2", "Author 2", 2021, 250, False),
    PrintedBook("Printed Book 3", "Author 3", 2019, 300, True),
    PrintedBook("Printed Book 4", "Author 4", 2021, 250, False),
    PrintedBook("Printed Book 5", "Author 5", 2019, 300, True),
    PrintedBook("Printed Book 6", "Author 6", 2021, 250, False),
    PrintedBook("Printed Book 7", "Author 7", 2019, 300, True),
    PrintedBook("Printed Book 8", "Author 8", 2021, 250, False),
    PrintedBook("Printed Book 9", "Author 9", 2019, 300, True),
    PrintedBook("Printed Book 10", "Author 10", 2021, 250, False),
]
all_books = ebooks + printed_books
for book in all_books:
    book.display_details()
