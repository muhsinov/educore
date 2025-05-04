import pytest
from address.models import Address
from group.models import Group
from lesson.models import Lesson
from course.models import Course
from user.models import Teacher, User


def test_homework_model():
    course = Course.objects.create(name = "programing",description = "ertgdsertgcff",cost = "56789")
    user = User.objects.create(first_name = "first_name",last_name = "last_name",birth_date = "2023-01-01",joined_at = "2023-01-01 12:00:00")
    address = Address.objects.create(street = "street",district = "district",region = "region",)
    group = Group.objects.create(name = "programing",course = course,room = 20,start_at = "2023-01-01 12:00:00",end_at = "2023-01-01 13:00:00")
    teacher = Teacher.objects.create(user = user,phone = "1234567890",address = address,salary = "56789",joined_at = "2023-01-01 12:00:00")
    lesson = Lesson.objects.create(name = "programing",description = "ertgdsertgcff",group = group,teacher = teacher,room = 20,file = "file.pdf",start_time = "2023-01-01 12:00:00",end_time = "2023-01-01 13:00:00")

    homework = lesson.homework_set.create(
        name = "homework",
        description = "ertgdsertgcff",
        lesson = lesson,
        deadline = "2023-01-01 12:00:00",
        created_at = "2023-01-01 12:00:00"
    )
    assert homework.name == "homework"
    assert homework.description == "ertgdsertgcff"
    assert homework.lesson == lesson
    assert homework.deadline == "2023-01-01 12:00:00"
    assert homework.created_at == "2023-01-01 12:00:00"