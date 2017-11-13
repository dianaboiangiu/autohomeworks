# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Course(models.Model):
    created_by = models.ForeignKey(User, related_name='owner')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User, related_name='courses',
                                     blank=True)

    def __str__(self):
        return 'Course {name}'.format(name=self.name)


class Material(models.Model):
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()


class Homework(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    test_file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()


class Solution(models.Model):
    homework = models.ForeignKey(Homework)
    user = models.ForeignKey(User)
    tests_status = models.CharField(max_length=200)
    tests_summary = models.CharField(max_length=400)
