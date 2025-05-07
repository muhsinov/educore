import unittest

from course.models import Course


class TestCourse(unittest.TestCase):
    def test_course(self):
        course = Course.objects.create(
            name="test course",
            description="test description",
            cost="100000",
            duration=30
        )
        self.assertEqual(course.name, "test course")
        self.assertEqual(course.description, "test description")
        self.assertEqual(course.cost, "100000")
        self.assertEqual(course.duration, 30)