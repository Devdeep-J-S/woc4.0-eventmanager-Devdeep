from django.shortcuts import render

from Event.models import Eventdata
from .forms import Participant_register_form
from .models import ParticipantData
# Create your views here.

from django.utils import timezone

# will be used in create list of event
l = Eventdata.objects.all()
data = []
for i in l:
    if (i.reg_deadline < timezone.now()):
        continue
    data.append(i)
    
def participant_registration_view(request):


    # creating list for participantes to view 
    contexts= {
    "events": data
}
    form = Participant_register_form(request.POST or None)  
    if form.is_valid():
        # another method to check whether participant can register for an event only once
        # e = form.cleaned_data['email_id']
        # event = form.cleaned_data['event_list']
        # l = []
        # l =ParticipantData.objects.all()
        # for i in l:
        #     if (i.email_id==e):
        #         if (i.event_list==event):
        #             return render(request,"participant_register_error.html", {}) 
        form.save()
        form = Participant_register_form() 
    contexts['form'] = form      
    return render(request,"register_participant.html",contexts)    