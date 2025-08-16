class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def __str__(self):
        return f"{self.title} by {self.author}"
class Library():
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return f"You checked out '{title}'."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' is not in the library."


    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return f"You returned '{title}'."
                else:
                    return f"'{title}' was not checked out."
        return f"'{title}' is not in the library."

    def list_available_books(self):
        available = [str(book) for book in self.__books if not book._is_checked_out]
        return available if available else ["No books available."]

