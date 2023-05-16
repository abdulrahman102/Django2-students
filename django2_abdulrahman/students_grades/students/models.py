from django.db import models


# Create your models here.

# ABDULRAHMAN USAMA
class Student(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    student_class = models.IntegerField(null=True)
    """def __str__(self):
        return f"{self.f_name} {self.l_name}"""


# ABDULRAHMAN USAMA
class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=255, null=True)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return f"{self.course_name}"


# model named Post
class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )
    # deﬁne a username ﬁeld with bound max length it can have
    username = models.CharField( max_length = 20, blank = False, null = False)
    # This is used to write a post
    text = models.TextField(blank = False, null = False)
    # Values for gender are restricted by giving choices
    gender = models.CharField(max_length = 6, choices =
    GENDER_CHOICES,
    default = Male)
    time = models.DateTimeField(auto_now_add = True)