
from datetime import date
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils.safestring import mark_safe
from .forms import EventForm
from .models import *
from .utils import Calender

# Create your views here.


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calender_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        
        d = get_date(self.request.GET.get('day', None))



        calender = Calender(d.year, d.month)

    
        html_calender = calender.formatmonth(withyear=True)
        context['calender'] = mark_safe(html_calender)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
  
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('calender:calendar')
        
    return render(request, 'register_calender.html', {'form': form})
def upcoming_event(request,id):
    calender=Event.objects.get(id=id)
    return render(request,"upcoming_event.html",{"upcoming_event":calender})

def edit_calender(request,id):
    calender=Event.objects.get(id=id)
    if request.method=="POST":
        form=Event(request.post,instance=calender)
        if form .is_valid():
            form.save
            return redirect("edit_calender.html",id=Event.id)
    else:
        form=Event(instance=calender)
    return render(request,"edit_calender.html",{"form":form})
