# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from homeworks.models import *

# Register your models here.

admin.site.register(Course)
admin.site.register(Homework)
admin.site.register(Material)
admin.site.register(Solution)