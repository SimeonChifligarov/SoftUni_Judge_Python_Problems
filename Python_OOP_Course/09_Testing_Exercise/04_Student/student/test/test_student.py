from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("SvetlinN", {"Python": ["pishi 6", "pishi 6", "pishi 6"]})

    def test_init_full_params(self):
        new_student = Student("Simeon", {"Python": ["uchi", "kodi", "testvai"]})
        self.assertEqual("Simeon", new_student.name)
        self.assertEqual({"Python": ["uchi", "kodi", "testvai"]}, new_student.courses)

    def test_init_without_param_courses(self):
        new_student = Student("Simo")
        self.assertEqual("Simo", new_student.name)
        self.assertEqual({}, new_student.courses)

    def test_init_with_none_param_for_courses(self):
        new_student = Student("Monka", None)
        self.assertEqual("Monka", new_student.name)
        self.assertEqual({}, new_student.courses)

    def test_enroll_existing_course_with_addcoursenotes(self):
        actual_result = self.student.enroll("Python", ["da", "be", "da"], "yes")
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6", "da", "be", "da"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", actual_result)

    def test_enroll_existing_course_without_addcoursenotes(self):
        actual_result = self.student.enroll("Python", ["ne", "be", "ne"])
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6", "ne", "be", "ne"]}, self.student.courses)
        self.assertEqual("Course already added. Notes have been updated.", actual_result)

    def test_enroll_nonexisting_course_without_addcoursenotes(self):
        actual_result = self.student.enroll("JS", ["dali", "ili"])
        self.assertEqual({"JS": ["dali", "ili"], "Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", actual_result)

    def test_enroll_nonexisting_course_with_addcoursenotes_empty(self):
        actual_result = self.student.enroll("JS", ["dali", "ili"], "")
        self.assertEqual({"JS": ["dali", "ili"], "Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", actual_result)

    def test_enroll_nonexisting_course_with_addcoursenotes_y(self):
        actual_result = self.student.enroll("JS", ["dali", "ili"], "Y")
        self.assertEqual({"JS": ["dali", "ili"], "Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", actual_result)

    def test_enroll_nonexisting_course_with_addcoursenotes_not_y(self):
        actual_result = self.student.enroll("JS", ["dali", "ili"], "Glupost")
        self.assertEqual({"JS": [], "Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        self.assertEqual("Course has been added.", actual_result)

    def test_add_notes_for_nonexisting_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", ["begai", "ot", "tuka"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)

    def test_add_notes_for_existing_course(self):
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        actual_result = self.student.add_notes("Python", "Evala brat")
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6", "Evala brat"]}, self.student.courses)
        self.assertEqual("Notes have been updated", actual_result)

    def test_leave_course_nonexisting_course(self):
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("C#")
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course_existing_course(self):
        self.assertEqual({"Python": ["pishi 6", "pishi 6", "pishi 6"]}, self.student.courses)
        actual_result = self.student.leave_course("Python")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", actual_result)


if __name__ == '__main__':
    main()
