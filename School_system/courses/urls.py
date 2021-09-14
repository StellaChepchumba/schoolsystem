from django.urls import path
from .views import edit_courses, register_courses,course_list,courses_details



urlpatterns=[
path('register/',register_courses,name='register_courses'),
path('course/',course_list,name='course_list'),
path('courses_details/<int:id>/',courses_details,name='courses_details'),
path('edit_courses/<int:id>/',edit_courses,name='edit_courses'),
]
