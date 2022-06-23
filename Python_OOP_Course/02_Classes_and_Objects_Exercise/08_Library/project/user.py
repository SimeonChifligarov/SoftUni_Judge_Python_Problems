# from project.library import Library


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        # rented_books_by_usernames = library.rented_books.values()
        if book_name not in library.books_available[author]:
            user_with_the_book = [u for u in library.rented_books if book_name in library.rented_books[u]][0]
            a = 5
            return f"The book \"{book_name}\" is already rented" \
                   f" and will be available in {library.rented_books[user_with_the_book][book_name]} days!"

        if book_name in library.books_available[author]:
            library.books_available[author].remove(book_name)

            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return

            self.books.append(book_name)

            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        del library.rented_books[self.username][book_name]
        if author not in library.books_available:
            library.books_available[author] = []
        library.books_available[author].append(book_name)

    def info(self):
        info_result = sorted(self.books)
        return ", ".join(info_result)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
