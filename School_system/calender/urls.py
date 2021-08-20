from django.urls import path
from .views import register_calender,calender_list



urlpatterns=[
    path('register/',register_calender,name='register_calender'),
    path('calender_list/',calender_list,name='calender_list'),
]

