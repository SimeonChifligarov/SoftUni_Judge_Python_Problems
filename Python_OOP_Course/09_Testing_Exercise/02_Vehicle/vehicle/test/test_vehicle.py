from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(69, 333)

    def test_init(self):
        new_vehicle = Vehicle(13.8, 666)
        self.assertEqual(13.8, new_vehicle.fuel)
        self.assertEqual(13.8, new_vehicle.capacity)
        self.assertEqual(666, new_vehicle.horse_power)
        self.assertEqual(1.25, new_vehicle.fuel_consumption)
        self.assertEqual(1.25, new_vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel(self):
        self.assertEqual(69, self.vehicle.fuel)
        self.vehicle.drive(4)
        self.assertEqual(64, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_too_much_fuel_after_driving(self):
        self.vehicle.fuel = 10
        self.assertEqual(10, self.vehicle.fuel)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(60)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_fuel(self):
        self.vehicle.fuel = 20
        self.assertEqual(20, self.vehicle.fuel)
        self.vehicle.refuel(5)
        self.assertEqual(25, self.vehicle.fuel)
        self.vehicle.refuel(15)
        self.assertEqual(40, self.vehicle.fuel)

    def test_repr(self):
        expected_result = f"The vehicle has 333 " \
               f"horse power with 69 fuel left and 1.25 fuel consumption"
        actual_result = str(self.vehicle)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
