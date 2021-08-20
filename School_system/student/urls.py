from django.urls import path
from .views import register_student, student_list



urlpatterns=[
    path('register/',register_student,name='register_student'),
    path('student_list/',student_list,name='student_list'),
]