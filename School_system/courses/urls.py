from django.urls import path
from .views import register_courses,course_list



urlpatterns=[
path('register/',register_courses,name='register_courses'),
path('course_list/',course_list,name='course_list'),
]
