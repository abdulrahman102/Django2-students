from django.urls import path
from . import views
from .views import StudentList

urlpatterns = [
path('studentcourse/', views.students_courses, name="studentcourse"),
path('courses/', views.courses, name='courses'),
path('students/', StudentList.as_view())
]
#ABDULRAHMAN USAMA