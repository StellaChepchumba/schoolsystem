from django.db import models

class Student(models.Model):
        first_name=models.CharField(max_length=12,null=True)
        last_name=models.CharField(max_length=12,null=True)
        age=models.PositiveSmallIntegerField()
        date_of_birth=models.DateField(max_length=10,null=True)
        roll_number=models.CharField(max_length=10,null=True)
        student_email=models.EmailField()
        nationality=(
        ("Kenyan","Kenyan"),
        ("Ugandan","Ugandan"),
        ("Rwandeese","Rwandees"),
        ("South Sudaneese","South Sudaneese"))
        nationality=models.CharField(max_length=15,choices=nationality)
        student_id=models.CharField(max_length=18,null=True)
        id_number=models.CharField(max_length=18,null=True)
        gender_choices=(
        ("Female","Female"),
        ("Male","Male")
        )
        gender=models.CharField(max_length=6,choices=gender_choices)
        phone_number=models.CharField(max_length=16,null=True)
        county=models.CharField(max_length=12,null=True)
        profile=models.ImageField(upload_to='documents/',null=True)
        medical_report=models.FileField()
        date_of_enrollment=models.DateField(max_length=8,null=True)
    # course_name=models.CharField(max_length=10)
        language_choices=(
        ("English","English"),
        ("Kiswahili","Kiswahili")
    )
        language=models.CharField(max_length=10,choices=language_choices)
        serial_number=models.CharField(max_length=10, blank=True, null=True)

# Create your models here.
