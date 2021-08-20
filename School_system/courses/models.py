from django.db import models
from django.db import models
from django.db.models.fields import CharField, DurationField
from django.db.models.fields.related import ManyToManyField
# from django.db import models

class Courses(models.Model):
        
        Course_name=models.CharField(max_length=12)
        Date_started=models.DateField()
        Syllabus=models.TextField()
        Course_id=models.CharField(max_length=12)
        Time_in_hours=models.DurationField()
        Course_code=models.CharField(max_length=12)
        # Course_Trainer=models.ManyToManyField()
        Course_duration=models.CharField(max_length=12)


# Create your models here.

# Create your models here.
