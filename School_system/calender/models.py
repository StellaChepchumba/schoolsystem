from django.db import models
from django.db import models
# from django.db import models

class Calender(models.Model):
    Events_id=models.CharField(max_length=12)
    Event_Name=models.CharField(max_length=12)
    Date_and_time=models.DateField(null=True,blank=True)
    Event_planner=models.CharField(max_length=12)
    # Event_duration=models.DurationField(null=True,blank=True)
    Event_participants=models.TextField(null=True,blank=True)
    Events_approved_by=models.CharField(max_length=12)
       
# Create your models here.


