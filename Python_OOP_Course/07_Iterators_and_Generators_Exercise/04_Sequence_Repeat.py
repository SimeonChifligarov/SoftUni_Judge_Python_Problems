class sequence_repeat:
    def __init__(self, seq, count):
        self.seq = seq
        self.count = count
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx >= self.count:
            raise StopIteration

        temp = self.current_idx
        self.current_idx += 1
        target_idx = temp % len(self.seq)
        return self.seq[target_idx]

# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
