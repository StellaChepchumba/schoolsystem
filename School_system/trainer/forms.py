from django import forms

from .models import Trainer


class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields ="__all__"
        widgets={}