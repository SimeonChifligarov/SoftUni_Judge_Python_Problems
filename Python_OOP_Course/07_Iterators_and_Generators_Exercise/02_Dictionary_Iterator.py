class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dictionary_elements = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        # initialization of helpers vars for iterator protocol in __iter__
        # but do not pass Judge tests
        # self.dictionary_elements = list(dictionary.items())
        # self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.dictionary_elements):
            raise StopIteration

        temp = self.index
        self.index += 1
        return self.dictionary_elements[temp]

# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)
