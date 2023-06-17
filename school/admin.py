from django.contrib import admin
from django.contrib.auth.models import Group
from school.models import Pupil
# Register your models here.

admin.site.unregister([Group])
admin.site.register(Pupil)