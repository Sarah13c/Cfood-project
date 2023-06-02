import pytest
from models import UserApp
from django.conf import settings
from django.urls import is_valid_path
def test_use_creation():
    user= UserApp.objects.create_user(
            username='test',
            email='test@gmail.com',
            name='testU',
    )

    assert user =='test'

@pytest.mark.urls("pytest_django_test.urls_overridden")
def test_urls() -> None:
    assert settings.ROOT_URLCONF == "no coge"
    assert is_valid_path("no sirve :D")
