from django.contrib import admin
from .models import Student, StudentAdmin
from.models import Teacher, TeacherAdmin

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher) # TeacherAdmin not needed __str__



