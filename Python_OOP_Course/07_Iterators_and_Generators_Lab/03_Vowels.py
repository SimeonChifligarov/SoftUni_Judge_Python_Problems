class vowels:
    def __init__(self, string):
        self.string = string
        self.i = 0
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.vowels_in_string = [ch for ch in self.string if ch.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.vowels_in_string):
            self.i += 1
            return self.vowels_in_string[self.i - 1]
        else:
            raise StopIteration

# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
