from django.contrib import admin
from calender.models import Event
# Register your models here.
from .models import Event
admin.site.register(Event)



