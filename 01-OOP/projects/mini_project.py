# Mini Project Hari Ini
# Class Book

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.year}"

# Tes
book1 = Book("Practical Statistics for Data Scientists", "Peter Bruce", 2020)
print(book1.get_info())
