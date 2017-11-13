# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course, Homework, Material, Solution

admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(Material)
admin.site.register(Solution)
