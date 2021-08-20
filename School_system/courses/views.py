from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from .forms import CoursesRegistrationForm
from .models import Courses 

# Create your views here.

def register_courses(request):
    if request.method=="POST":
        form=CoursesRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CoursesRegistrationForm()
    return render(request,"register_courses.html",{"form":form})

def course_list(request):
    courses=Courses.objects.all()
    return render(request,"course_list.html",{"course":courses})
# Create your views here.
