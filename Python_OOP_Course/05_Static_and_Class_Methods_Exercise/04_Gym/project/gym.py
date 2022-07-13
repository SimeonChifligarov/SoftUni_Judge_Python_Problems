from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription_info_result = []
        current_subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        current_customer = [c for c in self.customers if c.id == current_subscription.customer_id][0]
        current_trainer = [t for t in self.trainers if t.id == current_subscription.trainer_id][0]
        current_plan = [p for p in self.plans if p.id == current_subscription.exercise_id][0]
        current_equipment = [e for e in self.equipment if e.id == current_plan.equipment_id][0]

        subscription_info_result.extend([current_subscription, current_customer, current_trainer,
                                         current_equipment, current_plan])

        return "\n".join(repr(obj) for obj in subscription_info_result)
