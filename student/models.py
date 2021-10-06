from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ("name", "address")


class Teacher(models.Model):
    ROLES = [("teacher", "teacher"), ("head_master", "head_master")]

    school = models.ForeignKey(
        School,
        related_name="teachers",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    qualification = models.CharField(max_length=256)
    subjects = models.JSONField(default=list)
    role = models.CharField(max_length=256, default="teacher", choices=ROLES)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        School,
        related_name="students",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
