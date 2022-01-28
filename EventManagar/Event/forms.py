from django import forms
from .models import Eventdata

class Event_register_form(forms.ModelForm):
    class Meta:
        model = Eventdata
        fields = ("__all__")
        exclude = ()   