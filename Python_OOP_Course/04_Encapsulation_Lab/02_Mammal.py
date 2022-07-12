class Mammal:
    __kingdom = 'animals'

    def __init__(self, name, type_mammal, sound):
        self.name = name
        self.type = type_mammal
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
