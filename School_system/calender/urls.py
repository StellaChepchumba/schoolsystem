from django.urls import path
from . import views



urlpatterns = [
    path('calender/', views.CalendarView.as_view(), name='calendar'),
    path('forms/', views.event, name='calender_list'), 
    path('upcoming_event/<int:id>/',views.upcoming_event,name='upcoming_event'),
    path("edit/<int:id>/",views.edit_calender,name="edit_calender"),

]
