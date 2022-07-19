# class Car:
#     def __init__(self, make, model, fuel_consumption, fuel_capacity):
#         self.make = make
#         self.model = model
#         self.fuel_consumption = fuel_consumption
#         self.fuel_capacity = fuel_capacity
#         self.fuel_amount = 0
#
#     @property
#     def make(self):
#         return self.__make
#
#     @make.setter
#     def make(self, new_value):
#         if not new_value:
#             raise Exception("Make cannot be null or empty!")
#         self.__make = new_value
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, new_value):
#         if not new_value:
#             raise Exception("Model cannot be null or empty!")
#         self.__model = new_value
#
#     @property
#     def fuel_consumption(self):
#         return self.__fuel_consumption
#
#     @fuel_consumption.setter
#     def fuel_consumption(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel consumption cannot be zero or negative!")
#         self.__fuel_consumption = new_value
#
#     @property
#     def fuel_capacity(self):
#         return self.__fuel_capacity
#
#     @fuel_capacity.setter
#     def fuel_capacity(self, new_value):
#         if new_value <= 0:
#             raise Exception("Fuel capacity cannot be zero or negative!")
#         self.__fuel_capacity = new_value
#
#     @property
#     def fuel_amount(self):
#         return self.__fuel_amount
#
#     @fuel_amount.setter
#     def fuel_amount(self, new_value):
#         if new_value < 0:
#             raise Exception("Fuel amount cannot be negative!")
#         self.__fuel_amount = new_value
#
#     def refuel(self, fuel):
#         if fuel <= 0:
#             raise Exception("Fuel amount cannot be zero or negative!")
#         self.__fuel_amount += fuel
#         if self.__fuel_amount > self.__fuel_capacity:
#             self.__fuel_amount = self.__fuel_capacity
#
#     def drive(self, distance):
#         needed = (distance / 100) * self.__fuel_consumption
#
#         if needed > self.__fuel_amount:
#             raise Exception("You don't have enough fuel to drive!")
#
#         self.__fuel_amount -= needed
#
#
# # car = Car("a", "b", 1, 4)
# # car.make = ""
# # print(car)


from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('Ford', 'Focus', 8, 40)

    def test_init(self):
        new_car = Car('Mazda', 'CX-5', 10, 60)
        # make, model, fuel_consumption, fuel_capacity, fuel_amount
        expected_make = 'Mazda'
        expected_model = 'CX-5'
        expected_fuel_consumption = 10
        expected_fuel_capacity = 60
        expected_fuel_amount = 0

        self.assertEqual(expected_make, new_car.make)
        self.assertEqual(expected_model, new_car.model)
        self.assertEqual(expected_fuel_consumption, new_car.fuel_consumption)
        self.assertEqual(expected_fuel_capacity, new_car.fuel_capacity)
        self.assertEqual(expected_fuel_amount, new_car.fuel_amount)

    def test_make_setter_with_valid(self):
        expected_make_pre = 'Ford'
        self.assertEqual(expected_make_pre, self.car.make)

        self.car.make = 'BMW'
        expected_make_post = 'BMW'
        self.assertEqual(expected_make_post, self.car.make)

    def test_make_setter_with_invalid_should_raise(self):
        expected_make_pre = 'Ford'
        self.assertEqual(expected_make_pre, self.car.make)

        expected_assert_raises_message = 'Make cannot be null or empty!'

        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_model_setter_with_valid(self):
        expected_model_pre = 'Focus'
        self.assertEqual(expected_model_pre, self.car.model)

        self.car.model = 'Octavia'
        expected_model_post = 'Octavia'
        self.assertEqual(expected_model_post, self.car.model)

    def test_model_setter_with_invalid_should_raise(self):
        expected_model_pre = 'Focus'
        self.assertEqual(expected_model_pre, self.car.model)

        expected_assert_raises_message = 'Model cannot be null or empty!'

        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_fuel_consumption_setter_with_valid(self):
        expected_fuel_consumption_pre = 8
        self.assertEqual(expected_fuel_consumption_pre, self.car.fuel_consumption)

        self.car.fuel_consumption = 10
        expected_fuel_consumption_post = 10
        self.assertEqual(expected_fuel_consumption_post, self.car.fuel_consumption)

    def test_fuel_consumption_with_invalid_should_raise(self):
        expected_fuel_consumption_pre = 8
        self.assertEqual(expected_fuel_consumption_pre, self.car.fuel_consumption)

        expected_assert_raises_message = 'Fuel consumption cannot be zero or negative!'

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -13
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_fuel_capacity_setter_with_valid(self):
        expected_fuel_capacity_pre = 40
        self.assertEqual(expected_fuel_capacity_pre, self.car.fuel_capacity)

        self.car.fuel_capacity = 55
        expected_fuel_capacity_post = 55
        self.assertEqual(expected_fuel_capacity_post, self.car.fuel_capacity)

    def test_fuel_capacity_with_invalid_should_raise(self):
        expected_fuel_capacity_pre = 40
        self.assertEqual(expected_fuel_capacity_pre, self.car.fuel_capacity)

        expected_assert_raises_message = 'Fuel capacity cannot be zero or negative!'

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -133
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_fuel_amount_setter_with_valid(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        self.car.fuel_amount = 22
        expected_fuel_amount_post = 22
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

    def test_fuel_amount_with_invalid_should_raise(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        expected_assert_raises_message = 'Fuel amount cannot be negative!'

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -22
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_refuel_with_valid_under_max_capacity(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        self.car.refuel(25)
        expected_fuel_amount_post = 25
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

    def test_refuel_with_two_refuels_valid_under_max_capacity(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        self.car.refuel(15)
        expected_fuel_amount_post = 15
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

        self.car.refuel(15)
        expected_fuel_amount_post_two = 30
        self.assertEqual(expected_fuel_amount_post_two, self.car.fuel_amount)

    def test_refuel_with_valid_above_max_capacity(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        self.car.refuel(155)
        expected_fuel_amount_post = 40
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

    def test_refuel_with_invalid_should_raise(self):
        expected_assert_raises_message = 'Fuel amount cannot be zero or negative!'

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-12)
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_drive_with_valid_distance(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        expected_fuel_amount_post = 30
        self.car.fuel_amount = 30
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

        expected_fuel_amount_after_drive = 14
        self.car.drive(200)
        self.assertEqual(expected_fuel_amount_after_drive, self.car.fuel_amount)

    def test_drive_with_invalid_bigger_distance(self):
        expected_fuel_amount_pre = 0
        self.assertEqual(expected_fuel_amount_pre, self.car.fuel_amount)

        expected_fuel_amount_post = 40
        self.car.fuel_amount = 40
        self.assertEqual(expected_fuel_amount_post, self.car.fuel_amount)

        expected_assert_raises_message = 'You don\'t have enough fuel to drive!'

        with self.assertRaises(Exception) as ex:
            self.car.drive(1200)
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.drive(501)
        self.assertEqual(expected_assert_raises_message, str(ex.exception))


if __name__ == '__main__':
    main()
