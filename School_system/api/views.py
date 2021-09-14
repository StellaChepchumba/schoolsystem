from django.shortcuts import render
from .serializers import CoursesSerializer, EventSerializer, StudentSerializer, TrainerSerializer
from rest_framework import viewsets
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from calender.models import Event

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewset(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CoursesViewset(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer

class CalenderViewset(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    
# Create your views here.
