from datetime import date

import pytest

from course.models import Course
from group.models import Group


@pytest.mark.django_db
def test_create_group():
    course = Course.objects.create(
        name="Python Backend",
        description="Python Django course",
        cost=1000000
    )

    group = Group.objects.create(
        name="Backend 101",
        course=course,
        room="Room A",
        started_at=date(2025, 5, 1),
        end_at=date(2025, 8, 1)
    )

    assert group.name == "Backend 101"
    assert group.course == course
    assert group.room == "Room A"
    assert group.started_at == date(2025, 5, 1)
    assert group.end_at == date(2025, 8, 1)
    assert str(group) == "Backend 101 (Python Backend)"
