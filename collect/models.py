from django.conf import settings
from django.db import models

from .validators import validate_bags


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to="uploads/courses/")

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        ordering = ["-id"]

    def courses(self):
        return Course.objects.filter(loop__in=self.loop_set.all()).distinct()


class Person(models.Model):
    first_name = models.CharField(help_text="first name", max_length=200)
    last_name = models.CharField(help_text="last name", max_length=200, null=False, blank=True)
    notes = models.CharField(help_text="notes...", max_length=200, null=False, blank=True)
    lat = models.CharField(max_length=200, null=False, blank=True)
    lon = models.CharField(max_length=200, null=False, blank=True)
    image = models.FileField(upload_to="uploads/people/", null=False, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        if self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        else:
            return f"{self.first_name.capitalize()}"


class Loop(models.Model):
    date = models.DateField()
    wage = models.IntegerField()
    bags = models.FloatField(validators=[validate_bags])
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group.name.capitalize()} -- {self.date}"
