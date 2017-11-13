from django.contrib.auth.models import User

from factory import SubFactory
from factory.django import DjangoModelFactory

from homeworks import models


class UserFactory(DjangoModelFactory):

    class Meta:
        model = User


class CourseFactory(DjangoModelFactory):
    created_by = SubFactory(UserFactory)

    class Meta:
        model = models.Course
