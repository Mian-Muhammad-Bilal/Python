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
