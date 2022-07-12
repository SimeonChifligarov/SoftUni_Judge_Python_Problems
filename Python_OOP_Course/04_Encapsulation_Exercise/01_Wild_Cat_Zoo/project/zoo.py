class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        if worker_name not in [w.name for w in self.workers]:
            return f"There is no {worker_name} in the zoo"

        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"

    def pay_workers(self):
        money_needed_to_pay_wokers = sum([w.salary for w in self.workers])
        if self.__budget < money_needed_to_pay_wokers:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= money_needed_to_pay_wokers
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed_for_tending_animals = sum([a.money_for_care for a in self.animals])
        if self.__budget < money_needed_for_tending_animals:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= money_needed_for_tending_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_status_result = f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []

        for anim in self.animals:
            if type(anim).__name__ == "Lion":
                lions.append(anim)
            elif type(anim).__name__ == "Tiger":
                tigers.append(anim)
            elif type(anim).__name__ == "Cheetah":
                cheetahs.append(anim)

        animal_status_result += f"----- {len(lions)} Lions:\n"
        for l in lions:
            animal_status_result += f"{repr(l)}\n"
        animal_status_result += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            animal_status_result += f"{repr(t)}\n"
        animal_status_result += f"----- {len(cheetahs)} Cheetahs:\n"
        for c in cheetahs:
            animal_status_result += f"{repr(c)}\n"

        return animal_status_result.strip()

    def workers_status(self):
        workers_status_result = f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []

        for w in self.workers:
            if type(w).__name__ == "Keeper":
                keepers.append(w)
            elif type(w).__name__ == "Caretaker":
                caretakers.append(w)
            elif type(w).__name__ == "Vet":
                vets.append(w)

        workers_status_result += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            workers_status_result += f"{repr(k)}\n"
        workers_status_result += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            workers_status_result += f"{repr(c)}\n"
        workers_status_result += f"----- {len(vets)} Vets:\n"
        for v in vets:
            workers_status_result += f"{repr(v)}\n"

        return workers_status_result.strip()
