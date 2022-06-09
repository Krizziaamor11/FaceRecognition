from django.contrib import admin
from .models import Userinfo, Student, Attendace
# Register your models here.

admin.site.register(Userinfo)
admin.site.register(Student)
admin.site.register(Attendace)