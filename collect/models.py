from django.conf import settings
from django.db import models

from .validators import validate_bags


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/courses/")

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"💵{self.person_set.first()}"

    class Meta:
        ordering = ["-id"]

    def courses(self):
        return Course.objects.filter(loop__in=self.loop_set.all()).distinct()


class Person(models.Model):
    first_name = models.CharField(help_text="first name", max_length=200)
    last_name = models.CharField(help_text="last name", max_length=200, blank=True)
    notes = models.CharField(help_text="notes...", max_length=200, blank=True)
    lat = models.CharField(max_length=200, blank=True)
    lon = models.CharField(max_length=200, blank=True)
    group = models.ForeignKey(Party, on_delete=models.CASCADE, blank=True)
    image = models.FileField(upload_to="uploads/people/", blank=True)

    def __str__(self):
        if self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        else:
            return f"{self.first_name.capitalize()}"


class Loop(models.Model):
    wage = models.IntegerField(help_text="$$$")
    bags = models.FloatField(help_text="🎒🎒🎒🎒", validators=[validate_bags])
    date = models.DateField()
    group = models.ForeignKey(Party, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name.capitalize()} -- {self.date}"

    class Meta:
        ordering = ["-date"]
