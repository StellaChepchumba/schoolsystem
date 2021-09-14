from django.shortcuts import render
from django.shortcuts import render,redirect

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

def courses_details(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"courses_details.html",{"course":courses})
def edit_courses(request,id):
    courses=Courses.objects.get(id=id)
    if request.method=="POST":
        form=CoursesRegistrationForm(request.post,instance=courses)
        if form .is_valid():
            form.save
            return redirect("edit_courses.html",id=courses.id)
    else:
        form=CoursesRegistrationForm(instance=courses)
        return render(request,"edit_courses.html",{"form":form})
# Create your views here.
