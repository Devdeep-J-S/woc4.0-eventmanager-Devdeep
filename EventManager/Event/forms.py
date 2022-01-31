from cProfile import label
from dataclasses import fields
from pyexpat import model
from django import forms
from phonenumbers import ValidationResult
from .models import Eventdata

from Participant.models import ParticipantData
# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.forms import ValidationError

#for date time picker

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class Event_register_form(forms.ModelForm):
    class Meta:
        model = Eventdata
        fields = ('__all__')
        exclude = ()   
        widgets = { 'From' :DateTimePickerInput(),'To' :DateTimePickerInput(),'reg_deadline' :DateTimePickerInput() , 'host_password':forms.PasswordInput,'description':forms.Textarea(attrs={'rows':4, 'cols':15,'placeholder': 'Description of Event'}),}

class login_form (forms.Form):
        mail = forms.EmailField(label ="Enter your mail")
        password = forms.CharField(widget=forms.PasswordInput,label = "Enter your Password")
        def clean(self):
            mail = self.cleaned_data.get("mail")
            password = self.cleaned_data.get("password")
            l = []
            flag = True
            l = Eventdata.objects.all()
            for i in l:
                #print( form.cleaned_data.get("mail"), form.cleaned_data.get("password"))
                if (i.host_email==mail and i.host_password==password ) :
                    p = []
                    p = ParticipantData.objects.all()
                    for j in p:
                        if (j.event_list==(str(i.id)+i.name)):  
                                flag = False
            if (flag):
                raise ValidationError({'password':["Oops ,  You have entered wrong password or email",]}) 
                  

                #return render(request,"login_error.html",{})
      