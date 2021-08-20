from django import forms

from .models import Calender


class  CalenderRegistrationForm(forms.ModelForm):
    class Meta:
        model=Calender
        fields ="__all__"
        widgets={}