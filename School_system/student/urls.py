from django.urls import path
from .views import edit_student, register_student, student_list, student_profile



urlpatterns=[
    path('register/',register_student,name='register_student'),
    path('student_list/',student_list,name='student_list'),
    path("profile/<int:id>/",student_profile,name="student_profile"),
    path("edit/<int:id>/",edit_student,name="edit_student"),
]