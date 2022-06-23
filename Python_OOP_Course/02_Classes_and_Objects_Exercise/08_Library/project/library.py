# from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"

        self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        if user_id not in [u.user_id for u in self.user_records]:
            return f"There is no user with id = {user_id}!"

        current_user: User = [u for u in self.user_records if u.user_id == user_id][0]

        if new_username == current_user.username:
            return "Please check again the provided username - it should be different than the username used so far!"

        old_username = current_user.username
        current_user.username = new_username

        if old_username in self.rented_books:
            current_user_rented_books = self.rented_books[old_username]
            del self.rented_books[old_username]
            self.rented_books[new_username] = current_user_rented_books

        return f"Username successfully changed to: {new_username} for userid: {user_id}"
