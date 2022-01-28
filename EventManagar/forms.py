from django import forms
from .models import ParticipantData
from Event.models import Eventdata

from django.utils import timezone


class Participant_register_form(forms.ModelForm):
        # creating list for radio button 
    l = []
    l =Eventdata.objects.all()
    temp_CHOICES = []
    for i in l:
        if (i.reg_deadline < timezone.now()):
            continue
        temp_CHOICES.append((str(i.id)+(i.name),(i.name)+" - "+str(i.id)))
    CHOICES = tuple(temp_CHOICES)
    event_list = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
    registration_type = forms.ChoiceField(choices=(("Individual","Individual"),("Group","Group")),widget = forms.RadioSelect())
    class Meta:
        model = ParticipantData
        fields = ("__all__")