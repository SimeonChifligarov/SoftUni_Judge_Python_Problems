class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        el = self.data.pop()
        return el

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        result_str = f'[{", ".join(reversed(self.data))}]'
        return result_str
