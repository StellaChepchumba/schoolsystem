from django.shortcuts import render
from django.shortcuts import render

from django.shortcuts import render
from .forms import TrainerRegistrationForm
from .models import Trainer

# Create your views here.

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})

def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})
# Create your views here.

# Create your views here.
