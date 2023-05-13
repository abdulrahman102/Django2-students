from django.db import models


# Create your models here.

# ABDULRAHMAN USAMA
class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    student_class = models.IntegerField(null=True)


# ABDULRAHMAN USAMA
class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=255, null=True)
    students = models.ManyToManyField(Student)
