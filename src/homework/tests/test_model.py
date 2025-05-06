# import pytest
# from datetime import datetime
# from address.models import Address
# from group.models import Group
# from lesson.models import Lesson
# from course.models import Course
# from user.models import Teacher, User, Student
# from homework.models import Homework, StudentHomework


# @pytest.mark.django_db
# def test_homework_model():
#     course = Course.objects.create(name = "programing",description = "ertgdsertgcff",cost = "56789",duration=30)
#     user = User.objects.create(first_name = "first_name",last_name = "last_name",birth_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date(),joined_at = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"))
#     group = Group.objects.create(name = "programing",course = course,room = 20,started_at = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),end_at = datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S"))
#     teacher = Teacher.objects.create(user = user,salary = "56789",)
#     lesson = Lesson.objects.create(name = "programing",description = "ertgdsertgcff",group = group,teacher = teacher,room = 20,file = "file.pdf",start_time = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),end_time = datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S"))

#     homework = Homework.objects.create(
#         name = "homework",
#         description = "ertgdsertgcff",
#         lesson = lesson,
#         deadline = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),

#     )
#     assert homework.name == "homework"
#     assert homework.description == "ertgdsertgcff"
#     assert homework.lesson == lesson
#     assert homework.deadline is not None
#     assert homework.created_at is not None



# @pytest.mark.django_db
# def test_model_student_homework():
#     course = Course.objects.create(name="programing", description="ertgdsertgcff", cost="56789", duration=30)
#     user = User.objects.create(first_name="first_name", last_name="last_name",birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),phone='0987654321')
#     user1 = User.objects.create(first_name="name", last_name="name",birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),phone='1234567890')
#     group = Group.objects.create(name="programing", course=course, room=20,started_at=datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),end_at=datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S"))
#     teacher = Teacher.objects.create(user=user, salary="56789", )
#     lesson = Lesson.objects.create(name="programing", description="ertgdsertgcff", group=group, teacher=teacher,room=20, file="file.pdf", start_time=datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),end_time=datetime.strptime("2023-01-01 13:00:00", "%Y-%m-%d %H:%M:%S"))
#     homework = Homework.objects.create(name="homework",description="ertgdsertgcff",lesson=lesson,deadline=datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S"),)
#     student = Student.objects.create(user=user1)


#     student_homework = StudentHomework.objects.create(
#         homework = homework,
#         student = student,
#         text = "ertgdsertgcff",
#         file = "file.pdf",
#         grade = 3,
#         teacher_advice = "ertgdsertgcff",
#     )

#     assert student_homework.homework == homework
#     assert student_homework.student == student
#     assert student_homework.text == "ertgdsertgcff"
#     assert student_homework.file == "file.pdf"
#     assert student_homework.grade == 3
#     assert student_homework.teacher_advice == "ertgdsertgcff"
#     assert student_homework.sended_at is not None

