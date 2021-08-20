from django.shortcuts import render

from django.shortcuts import render
from .forms import CalenderRegistrationForm
from .models import Calender

# Create your views here.

def register_calender(request):
    if request.method=="POST":
        form=CalenderRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CalenderRegistrationForm()
    return render(request,"register_calender.html",{"form":form})

def calender_list(request):
    calenders=Calender.objects.all()
    return render(request,"calender_list.html",{"calenders":calenders})
# Create your views here.


# Create your views here.
