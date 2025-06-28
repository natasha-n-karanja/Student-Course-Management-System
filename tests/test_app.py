import unittest
from models.student import Student
from models.course import Course

class TestStudent(unittest.TestCase):
    def test_enroll_course(self):
        s = Student(1, "Tasha", "tasha@email.com")
        c = Course(101, "Math", 3)
        s.enroll(c)
        self.assertIn(c, s.course_history)

if __name__ == '__main__':
    unittest.main()
