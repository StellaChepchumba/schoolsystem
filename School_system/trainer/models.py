from django.db import models
# from django.db import models

class Trainer(models.Model):
        first_name=models.CharField(max_length=12)
        last_name=models.CharField(max_length=12)
        age=models.PositiveSmallIntegerField()
        date_of_birth=models.DateField(max_length=10)
        Languages=models.TextField(null=True,blank=True)
        Training_day=models.CharField(max_length=12)
        Email_address=models.EmailField(null=True,blank=True)
        Date_joined=models.DateField(null=True,blank=True)
        profile=models.ImageField(upload_to='documents/',null=True)
        Bio=models.TextField(null=True,blank=True)
        Contract=models.FileField()
        Date_hired=models.DateField(blank=True,null=True)
        # Courses=models.ManyToManyField()
        # Gender=models.Choices()
        def full_name(self):
                return f"{self.first_name} {self.last_name}"

# Create your models here.
