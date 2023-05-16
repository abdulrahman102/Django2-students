from django.contrib import admin
from .models import Student, Course, Post

# Register your models here.
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name") 

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "course_name") 



admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Post)