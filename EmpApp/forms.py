from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Skill, Certification, FuturePlan, Responce, LiveInteraction
from django.core.exceptions import ValidationError


RATING_CHOICE = (
    ('1','1 (I Have heard this one.)'),
    ('2','2 (Just started learning.)'),
    ('3','3 (Can builb something.)'),
    ('4','4 (Got a grip.)'),
    ('5','5 (Cup of tea for me......)'),
)

YES_NO = (
    (True, 'Should Do'),
    (False, 'Should Not Do')
)

class CustomUserCreationFormManager(forms.ModelForm):
    email = forms.EmailField(label='Enter Email')
    password = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'required':'false', 'style':'display:none'}))
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = CustomUser.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','department')


class CustomUserCreationFormEmployee(forms.ModelForm):
    email = forms.EmailField(label='Enter Email')
    password = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'required':'false', 'style':'display:none'}))
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = CustomUser.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)



class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields=['skill','rating']
        widgets = {
            'skill': forms.TextInput(attrs={'required': True, 'class':'form-control col-md-6' }),
            'rating': forms.RadioSelect(choices=RATING_CHOICE, attrs={'required': True})
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields=['title','certificate']
        widgets = {
            'title': forms.TextInput(attrs={'required': False, 'class':'form-control col-md-6' }),
            'certificate': forms.ClearableFileInput(attrs={'required': False})
        }

class FuturePlanForm(forms.ModelForm):
    class Meta:
        model = FuturePlan
        fields=['technology']
        widgets = {
            'technology': forms.TextInput(attrs={'required': True, 'class':'form-control col-md-6' }),
        }

class ResponceForm(forms.ModelForm):
    class Meta:
        model = Responce
        fields=['skill_development','suggession']
        widgets = {
            'skill_development': forms.RadioSelect(choices=YES_NO, attrs={'required': True }),
            'suggession': forms.TextInput(attrs={'required': True, 'class':'form-control col-md-6' }),
        }


class LiveInteractionForm(forms.ModelForm):
    class Meta:
        model = LiveInteraction

        fields=['topic','time_required', 'when', 'on']
        widgets = {
            'topic': forms.TextInput(attrs={'required': True, 'class':'form-control col-md-6' }),
            'time_required': forms.NumberInput(attrs={'required': True, 'class':'form-control time col-md-6' }),
            'when': forms.TextInput(attrs={'required': True, 'type':"datetime", 'class':'form-control time col-md-6' }),
            'on': forms.SelectDateWidget(attrs={'required': True, 'class':'form-control time col-md-6' }),
        }
