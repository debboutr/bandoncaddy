from django.contrib import admin

from .models import Course, Group, Loop, Person


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): ...


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin): ...


@admin.register(Loop)
class LoopAdmin(admin.ModelAdmin): ...


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin): ...
