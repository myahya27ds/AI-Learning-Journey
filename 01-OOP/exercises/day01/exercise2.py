import datetime

# Book Class
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def book_info(self):
        return f"This book is titled {self.title}, written by {self.author}, belongs to the {self.genre} genre, and was first published in {self.year}."

    def book_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

# --- Testing ---
book1 = Book("'Rich Dad, Poor Dad'", "Robert T.Kiyosaki", 2011, "Financial")
print(book1.book_info())
print("Book age:", book1.book_age(), "years")