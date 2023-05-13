from django.shortcuts import render
from .models import Student, Course
from django.views.generic.list import ListView
# Create your views here.

#ABDULRAHMAN USAMA
# Function-based method
def students_courses(request):
    context = {}
    context["students"] = Student.objects.all()
    context["courses"] = Course.objects.all()
    return render(request, "students_courses.html", context)
def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {'courses':courses})


# Class-based method
class StudentList(ListView):
    model = Student