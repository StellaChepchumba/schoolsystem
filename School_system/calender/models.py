from django.db import models
# from django.db import models
# from django.db import models

class Event(models.Model):
    Events_id=models.CharField(max_length=12)
    Event_Name=models.CharField(max_length=12)
    Event_planner=models.CharField(max_length=12)
    Event_participants=models.TextField(null=True,blank=True)
    Events_approved_by=models.CharField(max_length=12)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

