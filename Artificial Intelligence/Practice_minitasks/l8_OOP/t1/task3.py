class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")


class EBook(Book):
    def __init__(self, title, author, publication_year, file_size):
        # super().__init__(title, author, publication_year)
        self.file_size = file_size

    def display_details(self):
        super().display_details()
        print(f"File Size: {self.file_size} MB")


class PrintedBook(Book):
    def __init__(self, title, author, publication_year, num_pages, is_hardcover):
        # super().__init__(title, author, publication_year)
        self.num_pages = num_pages
        self.is_hardcover = is_hardcover

    def display_details(self):
        # super().display_details()
        print(f"Number of Pages: {self.num_pages}")
        print(f"Is Hardcover: {'Yes' if self.is_hardcover else 'No'}")


# Create instances of EBook
ebooks = [
    EBook(title="Python Basics", author="John Doe",
          publication_year=2020, file_size=2.5),
    EBook(title="Data Science Essentials", author="Jane Smith",
          publication_year=2018, file_size=3.0),
    # Add more EBook instances as needed
]

# Create instances of PrintedBook
printed_books = [
    PrintedBook(title="Intro to AI", author="Alan Turing",
                publication_year=1950, num_pages=300, is_hardcover=True),
    PrintedBook(title="History of Physics", author="Isaac Newton",
                publication_year=1687, num_pages=200, is_hardcover=False),
    # Add more PrintedBook instances as needed
]

# Combine both types of books into a single list
all_books = ebooks + printed_books

# Display details for each book using a for loop
for book in all_books:
    print("\nBook Details:")
    book.display_details()
