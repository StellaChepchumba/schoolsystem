from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from rest_framework.utils import field_mapping
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from calender.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age",)


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("first_name","last_name","age")

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=("Course_name","Course_code","Date_started")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("Event_Name","Events_id","Event_planner")

