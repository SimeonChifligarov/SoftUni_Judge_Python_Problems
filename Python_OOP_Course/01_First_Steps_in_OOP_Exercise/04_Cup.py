class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    @property
    def free_space(self):
        return self.size - self.quantity

    def fill(self, milliliters):
        if milliliters > self.free_space:
            return

        self.quantity += milliliters

    def status(self):
        return self.free_space
