# class Worker:
#
#     def __init__(self, name, salary, energy):
#         self.name = name
#         self.salary = salary
#         self.energy = energy
#         self.money = 0
#
#     def work(self):
#         if self.energy <= 0:
#             raise Exception('Not enough energy.')
#
#         self.money += self.salary
#         self.energy -= 1
#
#     def rest(self):
#         self.energy += 1
#
#     def get_info(self):
#         return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker('Berbatov', 100_000, 99)

    def test_init(self):
        new_worker = Worker('Rooney', 250_000, 101)
        self.assertEqual('Rooney', new_worker.name)
        self.assertEqual(250000, new_worker.salary)
        self.assertEqual(101, new_worker.energy)
        self.assertEqual(0, new_worker.money)

    def test_work_add_salary_to_money_when_correct(self):
        expected_result_money_pre = 0
        self.assertEqual(expected_result_money_pre, self.worker.money)
        self.worker.work()
        expected_result_money_post = 100_000
        self.assertEqual(expected_result_money_post, self.worker.money)

    def test_work_reduce_energy_when_correct(self):
        expected_result_energy_pre = 99
        self.assertEqual(expected_result_energy_pre, self.worker.energy)
        self.worker.work()
        expected_result_energy_post = 98
        self.assertEqual(expected_result_energy_post, self.worker.energy)

    def test_work_when_no_energy_should_raise(self):
        expected_result_energy_pre = 99
        self.assertEqual(expected_result_energy_pre, self.worker.energy)
        for _ in range(99):
            self.worker.work()
        expected_result_energy_post = 0
        self.assertEqual(expected_result_energy_post, self.worker.energy)

        with self.assertRaises(Exception) as ex:
            self.worker.work()
        expected_raises_message = 'Not enough energy.'
        self.assertEqual(expected_raises_message, str(ex.exception))

    def test_rest_add_energy(self):
        expected_energy_pre = 99
        self.assertEqual(expected_energy_pre, self.worker.energy)
        self.worker.rest()
        expected_energy_post = 100
        self.assertEqual(expected_energy_post, self.worker.energy)
        self.worker.rest()
        expected_energy_post = 101
        self.assertEqual(expected_energy_post, self.worker.energy)

    def test_get_info(self):
        expected_result = 'Berbatov has saved 0 money.'
        self.assertEqual(expected_result, self.worker.get_info())
        self.worker.money = 1_337_000
        expected_result_post = 'Berbatov has saved 1337000 money.'
        self.assertEqual(expected_result_post, self.worker.get_info())


if __name__ == '__main__':
    main()
