from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from calender.models import Event

def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Courses.objects.count() 
    calenders=Event.objects.count()
    data={"student":students,"trainer":trainers,"courses":courses,"events":calenders}
    return render(request,"home.html",data)
# Create your views here.
