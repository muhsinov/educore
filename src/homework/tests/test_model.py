import unittest
from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from address.models import Address
from group.models import Group
from lesson.models import Lesson
from course.models import Course
from user.models import Teacher, User, Student
from homework.models import Homework, StudentHomework

class TestHomeworkModels(TestCase):
    def setUp(self):
        # Umumiy sozlashlar
        self.course = Course.objects.create(
            name="programing",
            description="ertgdsertgcff",
            cost="56789",
            duration=30
        )
        self.user = User.objects.create(
            first_name="first_name",
            last_name="last_name",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            phone='0987654321',
            joined_at=timezone.datetime(2023, 1, 1, 12, 0, tzinfo=timezone.get_default_timezone())
        )
        self.user1 = User.objects.create(
            first_name="name",
            last_name="name",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            phone='1234567890'
        )
        naive_started_at = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        naive_end_at = datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S")
        started_at = timezone.make_aware(naive_started_at)
        end_at = timezone.make_aware(naive_end_at)
        self.group = Group.objects.create(
            name="programing",
            course=self.course,
            room=20,
            started_at=started_at,
            end_at=end_at
        )
        self.teacher = Teacher.objects.create(
            user=self.user,
            salary="56789"
        )
        self.student = Student.objects.create(
            user=self.user1
        )
        naive_start_time = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        naive_end_time = datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S")
        start_time = timezone.make_aware(naive_start_time)
        end_time = timezone.make_aware(naive_end_time)
        self.lesson = Lesson.objects.create(
            name="programing",
            description="ertgdsertgcff",
            group=self.group,
            teacher=self.teacher,
            room=20,
            file="file.pdf",
            start_time=start_time,
            end_time=end_time
        )

    def test_homework_model(self):
        # Homework modelini sinash
        deadline = timezone.datetime(2023, 1, 1, 12, 0, tzinfo=timezone.get_default_timezone())
        homework = Homework.objects.create(
            name="homework",
            description="ertgdsertgcff",
            lesson=self.lesson,
            deadline=deadline
        )
        self.assertEqual(homework.name, "homework")
        self.assertEqual(homework.description, "ertgdsertgcff")
        self.assertEqual(homework.lesson, self.lesson)
        self.assertIsNotNone(homework.deadline)
        self.assertIsNotNone(homework.created_at)

    def test_model_student_homework(self):
        # StudentHomework modelini sinash
        deadline = timezone.datetime(2023, 1, 1, 12, 0, tzinfo=timezone.get_default_timezone())
        homework = Homework.objects.create(
            name="homework",
            description="ertgdsertgcff",
            lesson=self.lesson,
            deadline=deadline
        )
        student_homework = StudentHomework.objects.create(
            homework=homework,
            student=self.student,
            text="ertgdsertgcff",
            file="file.pdf",
            grade=3,
            teacher_advice="ertgdsertgcff"
        )
        self.assertEqual(student_homework.homework, homework)
        self.assertEqual(student_homework.student, self.student)
        self.assertEqual(student_homework.text, "ertgdsertgcff")
        self.assertEqual(student_homework.file, "file.pdf")
        self.assertEqual(student_homework.grade, 3)
        self.assertEqual(student_homework.teacher_advice, "ertgdsertgcff")
        self.assertIsNotNone(student_homework.sended_at)