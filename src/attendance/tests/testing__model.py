import unittest
from datetime import datetime
from django.test import TestCase
from address.models import Address
from attendance.models import Attendance
from lesson.models import Lesson
from course.models import Course
from user.models import Teacher, User, Student
from group.models import Group

class TestAttendanceModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="programing",
            description="ertgdsertgcff",
            cost="56789",
            duration=30
        )
        self.address = Address.objects.create(
            street="test street",
            destrict="test district",
            region="test region"
        )
        self.address1 = Address.objects.create(
            street="street",
            destrict="district",
            region="region"
        )
        self.user = User.objects.create(
            first_name="first_name",
            last_name="last_name",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            phone='0987654345',
            address=self.address
        )
        self.user1 = User.objects.create(
            first_name="first_name",
            last_name="last_name",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            phone='345678943',
            address=self.address1
        )
        self.group = Group.objects.create(
            name="programing",
            course=self.course,
            room=20,
            started_at=datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
            end_at=datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S")
        )
        self.teacher = Teacher.objects.create(
            user=self.user,
            salary="56789"
        )
        self.student = Student.objects.create(
            user=self.user1
        )
        self.lesson = Lesson.objects.create(
            name="programing",
            description="ertgdsertgcff",
            group=self.group,
            teacher=self.teacher,
            room=20,
            file="file.pdf",
            start_time=datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),
            end_time=datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S")
        )
        self.attendance = Attendance.objects.create(
            lesson=self.lesson,
            student=self.student,
            status=True
        )

    def test_attendance_model(self):
        self.assertEqual(self.attendance.lesson, self.lesson)
        self.assertEqual(self.attendance.student, self.student)
        self.assertEqual(self.attendance.status, True)
        self.assertIsNotNone(self.attendance.time)

