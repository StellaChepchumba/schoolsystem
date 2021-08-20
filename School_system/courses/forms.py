from django import forms

from .models import Courses


class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields ="__all__"
        widgets={}