from django import forms
from .models import TimeSheet
from django.core.exceptions import ValidationError



class TimeSheetForm(forms.ModelForm):

    class Meta:
        model = TimeSheet
        fields=['task','subTask','timeSpend']
        widgets = {
            'task': forms.Select(attrs={'required': True, 'class':'form-control col-md-6' }),
            'subTask': forms.TextInput(attrs={'required': True, 'class':'form-control col-md-6' }),
            'timeSpend': forms.NumberInput(attrs={'required': True, 'class':'form-control col-md-6' })
        }
