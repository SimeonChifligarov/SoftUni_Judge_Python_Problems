from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Grubby", "Orc", "I am better")

    def test_init(self):
        new_mammal = Mammal("Insomnia", "Human", "I am the best")
        self.assertEqual("Insomnia", new_mammal.name)
        self.assertEqual("Human", new_mammal.type)
        self.assertEqual("I am the best", new_mammal.sound)
        self.assertEqual("animals", new_mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = "Grubby makes I am better"
        actual_result = self.mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        expected_result = "animals"
        actual_result = self.mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)

    def test_info(self):
        expected_result = "Grubby is of type Orc"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
