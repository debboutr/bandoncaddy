from django.contrib import admin

from .models import Course, Party, Loop, Person


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): ...


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin): ...


@admin.register(Loop)
class LoopAdmin(admin.ModelAdmin): ...


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin): ...
