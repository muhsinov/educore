from django.test import TestCase
from django.utils import timezone
from datetime import time
from group.models import Group
from ..models import Lesson, Grade
from course.models import Course
from user.models import User, Student, Teacher 

class TestLessonModel(TestCase):
    def setUp(self):
        user = User.objects.create_user(phone="998901112233", password="test123")
        self.teacher = Teacher.objects.create(user=user, salary=100000.00)
        
        self.course = Course.objects.create(
            name="Physics",
            description="Physics course",
            cost=50000,
            duration=30
        )

        self.group = Group.objects.create(
            name="Test Group",
            course =self.course,
            started_at=timezone.now(), 
            end_at=timezone.now() + timezone.timedelta(hours=1) 
        )
        
        self.lesson = Lesson.objects.create(
            name="Math",
            description="Algebra and Geometry",
            group=self.group,
            teacher=self.teacher,
            room="101-A",
            file=None,
            start_time=time(9, 0),
            end_time=time(10, 30)
        )

    def test_lesson_str(self):
        self.assertEqual(str(self.lesson), "Math")
        self.assertEqual(self.lesson.description, "Algebra and Geometry")
        self.assertEqual(self.lesson.group.name, "Test Group")
        self.assertEqual(self.lesson.teacher.user.phone, "998901112233")
        self.assertEqual(self.lesson.room, "101-A")
        self.assertEqual(self.lesson.file, None)
        self.assertEqual(self.lesson.start_time, time(9, 0))
        self.assertEqual(self.lesson.end_time, time(10, 30))
        self.assertEqual(self.lesson.group.course.name, "Physics")
        self.assertEqual(self.lesson.group.course.description, "Physics course")
        self.assertEqual(self.lesson.group.course.cost, 50000)
        self.assertEqual(self.lesson.group.course.duration, 30)

class TestGradeModel(TestCase):
    def setUp(self):
        student_user = User.objects.create_user(phone="998909998877", password="test456")
        self.student = Student.objects.create(user=student_user)

        teacher_user = User.objects.create_user(phone="998901234567", password="test789")
        self.teacher = Teacher.objects.create(user=teacher_user, salary=100000.00)
        
        self.course = Course.objects.create(
            name="Physics",
            description="Physics course",
            cost=50000,
            duration=30
        )

        self.group = Group.objects.create(
            name="Grade Group",
            course=self.course,
            started_at=timezone.now(),
            end_at=timezone.now() + timezone.timedelta(hours=1)
        )
        self.lesson = Lesson.objects.create(
            name="Physics",
            description="Mechanics",
            group=self.group,
            teacher=self.teacher,
            room="302-B",
            file=None,
            start_time=time(11, 0),
            end_time=time(12, 30)
        )
        self.grade = Grade.objects.create(
            lesson=self.lesson,
            student=self.student,
            grade=4
        )

    def test_grade_str(self):
        self.assertEqual(str(self.grade), f"{self.student} - {self.lesson}: 4")
        self.assertEqual(self.grade.lesson.name, "Physics")
        self.assertEqual(self.grade.student.user.phone, "998909998877")
        self.assertEqual(self.grade.grade, 4)
        self.assertEqual(self.grade.lesson.group.name, "Grade Group")
        self.assertEqual(self.grade.lesson.teacher.user.phone, "998901234567")
        self.assertEqual(self.grade.lesson.room, "302-B")
        self.assertEqual(self.grade.lesson.file, None)
        self.assertEqual(self.grade.lesson.start_time, time(11, 0))
        self.assertEqual(self.grade.lesson.end_time, time(12, 30))
        self.assertEqual(self.grade.lesson.group.course.name, "Physics")
        self.assertEqual(self.grade.lesson.group.course.description, "Physics course")
        self.assertEqual(self.grade.lesson.group.course.cost, 50000)
        self.assertEqual(self.grade.lesson.group.course.duration, 30)
        self.assertEqual(self.grade.lesson.group.course, self.course)
        self.assertEqual(self.grade.lesson.group, self.group)
        self.assertEqual(self.grade.lesson.teacher, self.teacher)
        self.assertEqual(self.grade.lesson.teacher.salary, 100000.00)
        self.assertEqual(self.grade.lesson.teacher.user.phone, "998901234567")
        self.assertEqual(self.grade.lesson.teacher.user.is_active, True)
        self.assertEqual(self.grade.lesson.teacher.user.is_staff, False)