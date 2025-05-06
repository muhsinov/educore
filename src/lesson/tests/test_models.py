# lesson/tests/test_models.py

from django.test import TestCase
from lesson.models import Lesson
from group.models import Group
from user.models import Teacher

from datetime import date

class LessonModelTest(TestCase):
    def setUp(self):
        self.group = Group.objects.create(name="Test Group")  # yoki kerakli fieldlar bilan
        self.teacher = Teacher.objects.create(full_name="Test Teacher")  # yoki kerakli fieldlar bilan

        self.lesson = Lesson.objects.create(
            name="Django Basics",
            description="Intro to Django",
            group=self.group,
            teacher=self.teacher,
            room="101A",
            file="lessons/test.pdf",  # real file bo‘lishi shart emas test uchun
            start_time=date(2024, 5, 5),
            end_time=date(2024, 5, 6)
        )

    def test_lesson_creation(self):
        self.assertEqual(self.lesson.name, "Django Basics")

    def test_lesson_str(self):
        self.assertEqual(str(self.lesson), "Django Basics")
