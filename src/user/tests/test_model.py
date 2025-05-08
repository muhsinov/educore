import pytest
from django.contrib.auth import get_user_model
from user.models import *
from address.models import Address
import datetime




def test_user():
    address = Address.objects.create(
        street="test street",
        destrict="test district",
        region="test region"
    )
    user = User.objects.create(
        phone="0987654321",
        first_name="first_name",
        last_name="last_name",
        birth_date=datetime.strptime("2023-01-01", "%Y-%m-%d").date(),
        address=address
    )
    assert user.phone == "0987654321"
    assert user.first_name == "first_name"
    assert user.last_name == "last_name"
    assert user.birth_date == datetime.strptime("2023-01-01", "%Y-%m-%d").date()
    assert user.address == address
    assert user.joined_at is not None
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False

