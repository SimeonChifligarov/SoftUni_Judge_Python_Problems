class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.i = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= 0:
            self.i -= 1
            return self.iterable[self.i + 1]
        else:
            raise StopIteration

# reversed_list = reverse_iter([1, 2, 3, 4])
# for item in reversed_list:
#     print(item)
