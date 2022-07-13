class Customer:
    def __init__(self, name, age, customer_id):
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds = []

    def __repr__(self):
        dvd_names = [d.name for d in self.rented_dvds]
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join(dvd_names)})"
