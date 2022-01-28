from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Eventdata

class Event_register_form(forms.ModelForm):
    class Meta:
        model = Eventdata
        fields = ("__all__")
        exclude = ()   

class login_form (forms.Form):
        mail = forms.EmailField(label ="Enter your mail")
        password = forms.CharField(widget=forms.PasswordInput,label = "Enter your Password")
      