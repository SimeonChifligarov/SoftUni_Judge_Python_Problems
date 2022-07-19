# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         self.fed = False
#         self.sleepy = False
#         self.size = 0
#
#     def eat(self):
#         if self.fed:
#             raise Exception('Already fed.')
#
#         self.fed = True
#         self.sleepy = True
#         self.size += 1
#
#     def sleep(self):
#         if not self.fed:
#             raise Exception('Cannot sleep while hungry')
#
#         self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat('Puh40')

    def test_init(self):
        new_cat = Cat('Purrr')
        expected_name = 'Purrr'
        expected_fed = False
        expected_sleepy = False
        expected_size = 0
        self.assertEqual(expected_name, new_cat.name)
        self.assertEqual(expected_fed, new_cat.fed)
        self.assertEqual(expected_sleepy, new_cat.sleepy)
        self.assertEqual(expected_size, new_cat.size)

    def test_eat_when_correct_ie_not_fed(self):
        expected_fed_pre = False
        self.assertEqual(expected_fed_pre, self.cat.fed)
        expected_sleepy_pre = False
        expected_size_pre = 0
        self.assertEqual(expected_sleepy_pre, self.cat.sleepy)
        self.assertEqual(expected_size_pre, self.cat.size)

        self.cat.eat()
        expected_fed_post = True
        expected_size_post = 1
        self.assertEqual(expected_fed_post, self.cat.fed)
        self.assertEqual(expected_size_post, self.cat.size)

    def test_eat_when_already_fed_should_raises(self):
        # expected_fed_pre = False
        # self.assertEqual(expected_fed_pre, self.cat.fed)
        # expected_sleepy_pre = False
        # expected_size_pre = 0
        # self.assertEqual(expected_sleepy_pre, self.cat.sleepy)
        # self.assertEqual(expected_size_pre, self.cat.size)
        #
        # self.cat.eat()
        # expected_fed_post = True
        # expected_size_post = 1
        # self.assertEqual(expected_fed_post, self.cat.fed)
        # self.assertEqual(expected_size_post, self.cat.size)

        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        expected_assert_raises_message = 'Already fed.'
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_sleep_when_eat_ie_correct(self):
        expected_sleepy_before_eat = False
        expected_fed_before_eat = False
        self.assertEqual(expected_sleepy_before_eat, self.cat.sleepy)
        self.assertEqual(expected_fed_before_eat, self.cat.fed)

        self.cat.eat()
        expected_sleepy_after_eat = True
        expected_fed_after_eat = True
        self.assertEqual(expected_sleepy_after_eat, self.cat.sleepy)
        self.assertEqual(expected_fed_after_eat, self.cat.fed)

        self.cat.sleep()
        expected_sleepy_after_sleep = False
        self.assertEqual(expected_sleepy_after_sleep, self.cat.sleepy)

    def test_sleep_when_not_fed_should_raises(self):
        expected_fed = False
        self.assertEqual(expected_fed, self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        expected_assert_raises_message = 'Cannot sleep while hungry'
        self.assertEqual(expected_assert_raises_message, str(ex.exception))


if __name__ == '__main__':
    main()
