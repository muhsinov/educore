import unittest
from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from course.models import Course
from group.models import Group, StudentGroup
from payment.models import Payment
from user.models import User, Student

class TestPaymentModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name="programing",
            description="ertgdsertgcff",
            cost="56789",
            duration=30
        )

        naive_started_at = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
        naive_end_at = datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S")
        self.started_at = timezone.make_aware(naive_started_at)
        self.end_at = timezone.make_aware(naive_end_at)

        self.group = Group.objects.create(
            name="programing",
            course=self.course,
            room=20,
            started_at=self.started_at,
            end_at=self.end_at
        )

        self.user = User.objects.create(
            first_name="first_name",
            last_name="last_name",
            birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
            phone='0987654321'
        )

        self.student = Student.objects.create(
            user=self.user
        )

        self.student_group = StudentGroup.objects.create(
            group_id=self.group,
            student_id=self.student,
            status=False
        )

    def test_payment(self):
        payment = Payment.objects.create(
            student_course=self.student_group,
            amount=1000000.32,
            type=0
        )
        self.assertEqual(payment.student_course, self.student_group)
        self.assertEqual(payment.amount, 1000000.32)
        self.assertEqual(payment.type, 0)
        self.assertIsNotNone(payment.payment_date)
