class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError(self.__username_value_error_message())
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError(self.__password_value_error_message())
        if not any(el.isupper() for el in value):
            raise ValueError(self.__password_value_error_message())
        if not any(el.isdigit() for el in value):
            raise ValueError(self.__password_value_error_message())

        self.__password = value

    @staticmethod
    def __username_value_error_message():
        return "The username must be between 5 and 15 characters."

    @staticmethod
    def __password_value_error_message():
        return "The password must be 8 or more characters with at least 1 digit and 1 uppercase letter."

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
