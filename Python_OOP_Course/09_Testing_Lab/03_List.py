# class IntegerList:
#     def __init__(self, *args):
#         self.__data = []
#         for x in args:
#             if type(x) == int:
#                 self.__data.append(x)
#
#     def get_data(self):
#         return self.__data
#
#     def add(self, element):
#         if not type(element) == int:
#             raise ValueError("Element is not Integer")
#         self.get_data().append(element)
#         return self.get_data()
#
#     def remove_index(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         a = self.get_data()[index]
#         del self.get_data()[index]
#         return a
#
#     def get(self, index):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         return self.get_data()[index]
#
#     def insert(self, index, el):
#         if index >= len(self.get_data()):
#             raise IndexError("Index is out of range")
#         elif not type(el) == int:
#             raise ValueError("Element is not Integer")
#
#         self.get_data().insert(index, el)
#
#     def get_biggest(self):
#         a = sorted(self.get_data(), reverse=True)
#         return a[0]
#
#     def get_index(self, el):
#         return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.int_ll = IntegerList(3, 5, 7, 9, 1)

    def test_init(self):
        new_int_ll = IntegerList('two', -3, -5, 7, 9, 1, [1, 2], 2.22, {'one': 1, 'eleven': 11})
        expected_int_ll = [-3, -5, 7, 9, 1]
        self.assertEqual(expected_int_ll, new_int_ll._IntegerList__data)

    def test_get_data(self):
        expected_data = [3, 5, 7, 9, 1]
        self.assertEqual(expected_data, self.int_ll.get_data())

    def test_add_with_int_ie_correct(self):
        expected_data = [3, 5, 7, 9, 1]
        self.assertEqual(expected_data, self.int_ll.get_data())
        actual_result = self.int_ll.add(1337)
        expected_data_post = [3, 5, 7, 9, 1, 1337]
        self.assertEqual(expected_data_post, actual_result)

    def test_add_two_times_in_a_roll_with_int(self):
        expected_data = [3, 5, 7, 9, 1]
        self.assertEqual(expected_data, self.int_ll.get_data())
        actual_result = self.int_ll.add(13)
        expected_data_post = [3, 5, 7, 9, 1, 13]
        self.assertEqual(expected_data_post, actual_result)
        actual_result_two = self.int_ll.add(37)
        expected_data_post_two = [3, 5, 7, 9, 1, 13, 37]
        self.assertEqual(expected_data_post_two, actual_result_two)

    def test_add_with_no_int_should_raises(self):
        assert_raises_expected_message = 'Element is not Integer'

        with self.assertRaises(ValueError) as ex_1:
            self.int_ll.add('69')
        self.assertEqual(assert_raises_expected_message, str(ex_1.exception))

        with self.assertRaises(ValueError) as ex_2:
            self.int_ll.add([2, 22])
        self.assertEqual(assert_raises_expected_message, str(ex_2.exception))

        with self.assertRaises(ValueError) as ex_3:
            self.int_ll.add({'one': 1, 'more': 1_000})
        self.assertEqual(assert_raises_expected_message, str(ex_3.exception))

    def test_remove_index_when_correct(self):
        expected_len_pre = 5
        actual_len_pre = len(self.int_ll.get_data())
        self.assertEqual(expected_len_pre, actual_len_pre)

        remove_index = 2
        actual_result_with_remove_index_2 = self.int_ll.remove_index(remove_index)
        expected_result_with_remove_index_2 = 7
        expected_get_data_after_remove = [3, 5, 9, 1]
        self.assertEqual(expected_result_with_remove_index_2, actual_result_with_remove_index_2)
        self.assertEqual(expected_get_data_after_remove, self.int_ll.get_data())

    def test_remove_index_when_valid_negative(self):
        expected_len_pre = 5
        actual_len_pre = len(self.int_ll.get_data())
        self.assertEqual(expected_len_pre, actual_len_pre)

        remove_index = -3
        actual_result_with_remove_index_2 = self.int_ll.remove_index(remove_index)
        expected_result_with_remove_index_2 = 7
        expected_get_data_after_remove = [3, 5, 9, 1]
        self.assertEqual(expected_result_with_remove_index_2, actual_result_with_remove_index_2)
        self.assertEqual(expected_get_data_after_remove, self.int_ll.get_data())

    def test_remove_index_when_invalid_bigger_should_raise(self):
        expected_len_pre = 5
        actual_len_pre = len(self.int_ll.get_data())
        self.assertEqual(expected_len_pre, actual_len_pre)

        with self.assertRaises(IndexError) as ex:
            self.int_ll.remove_index(11)

        assert_raises_expected_message = 'Index is out of range'

        self.assertEqual(assert_raises_expected_message, str(ex.exception))

    def test_get_with_valid_index(self):
        expected_result_with_index_0 = 3
        expected_result_with_index_1 = 5
        expected_result_with_index_2 = 7
        expected_result_with_index_negative_1 = 1
        self.assertEqual(expected_result_with_index_0, self.int_ll.get(0))
        self.assertEqual(expected_result_with_index_1, self.int_ll.get(1))
        self.assertEqual(expected_result_with_index_2, self.int_ll.get(2))
        self.assertEqual(expected_result_with_index_negative_1, self.int_ll.get(-1))

    def test_get_when_invalid_bigger_should_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.int_ll.get(33)

        assert_raises_expected_message = 'Index is out of range'

        self.assertEqual(assert_raises_expected_message, str(ex.exception))

    def test_insert_with_valid_data(self):
        expected_starting_data = [3, 5, 7, 9, 1]
        self.assertEqual(expected_starting_data, self.int_ll._IntegerList__data)

        expected_data_after_one = [3, 5, 7, -333, 9, 1]
        self.int_ll.insert(3, -333)
        actual_data_after_one = self.int_ll.get_data()
        self.assertEqual(expected_data_after_one, actual_data_after_one)

        expected_data_after_two = [333, 3, 5, 7, -333, 9, 1]
        self.int_ll.insert(0, 333)
        actual_data_after_two = self.int_ll.get_data()
        self.assertEqual(expected_data_after_two, actual_data_after_two)

    def test_insert_with_invalid_bigger_index_should_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.int_ll.insert(44, 202)

        assert_raises_expected_message = 'Index is out of range'

        self.assertEqual(assert_raises_expected_message, str(ex.exception))

    def test_insert_with_invalid_data_type_should_raise(self):
        expected_assert_raises_message = 'Element is not Integer'

        with self.assertRaises(ValueError) as ex_1:
            self.int_ll.insert(0, '1')
        self.assertEqual(expected_assert_raises_message, str(ex_1.exception))

        with self.assertRaises(ValueError) as ex_2:
            self.int_ll.insert(0, 13.37)
        self.assertEqual(expected_assert_raises_message, str(ex_2.exception))

        with self.assertRaises(ValueError) as ex_3:
            self.int_ll.insert(0, ['a', 'b', 'c'])
        self.assertEqual(expected_assert_raises_message, str(ex_3.exception))

        with self.assertRaises(ValueError) as ex_4:
            self.int_ll.insert(0, [-1, -2, -3])
        self.assertEqual(expected_assert_raises_message, str(ex_4.exception))

    def test_get_biggest(self):
        expected_biggest = 9
        actual_result_biggest = self.int_ll.get_biggest()

        self.assertEqual(expected_biggest, actual_result_biggest)

    def test_get_index(self):
        expected_get_with_el_3 = 0
        expected_get_with_el_5 = 1
        expected_get_with_el_7 = 2

        self.assertEqual(expected_get_with_el_3, self.int_ll.get_index(3))
        self.assertEqual(expected_get_with_el_5, self.int_ll.get_index(5))
        self.assertEqual(expected_get_with_el_7, self.int_ll.get_index(7))


if __name__ == '__main__':
    main()
