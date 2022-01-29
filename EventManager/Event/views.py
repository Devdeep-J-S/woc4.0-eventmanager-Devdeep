from django.shortcuts import render

# Create your views here.
from time import strftime
from django.http import HttpResponse
from .forms import Event_register_form ,login_form
from .models import Eventdata

# Create your views here.
def home_view(request):
    return render(request,"base.html",{})

def event_registration_view(request):
    form = Event_register_form(request.POST or None)  
    if form.is_valid():
        # another way to tackle the problem of end date < From date 
        # # x = form.cleaned_data['From']
        # # y= form.cleaned_data['To']
        # # if (x == y):
        # #     return render(request,"event_registeration_error.html",{}) 
        # # else:    
        # def clean(self):
        #     if self.start_date > self.end_date:
        #         raise ValidationError('Start date is after end date')
        form.save()
        # mail the host 
        # another way to mail the host
        # start_date = form.cleaned_data['From'].strftime("%m/%d/%Y, %H:%M:%S")
        # end_date =  form.cleaned_data['To'].strftime("%m/%d/%Y, %H:%M:%S")
        # reg_date =  form.cleaned_data['reg_deadline'].strftime("%m/%d/%Y, %H:%M:%S")
        # subject = 'Thank you for using our site for your event registration.'
        # message = 'It  means a world to us \nThe Event details:\n' +' Your Event name is ' +  form.cleaned_data['name'] +'.\n'+'Event Description: ' +  form.cleaned_data['description'] +'.\n' + ' Your Event\'s poster link is ' +  form.cleaned_data['link'] +'.\n' +'Event starting date :'+start_date+'.\n' +'Event ending date :'+end_date+'.\n'+'Event registration deadline :'+reg_date+'.\n' 
        # # = 
        
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = []
        # recipient_list.append( form.cleaned_data['host_email'])
        # send_mail( subject, message, email_from, recipient_list )
        form = Event_register_form()    
    return render(request,"register_event.html", {'form':form })    
   
def login_view(request):
    form =  login_form(request.POST or None)
    l = []
    l = Eventdata.objects.all()
    for i in l:
        if form.is_valid():
            #print( form.cleaned_data.get("mail"), form.cleaned_data.get("password"))
            if (i.host_email==form.cleaned_data.get("mail") and i.host_password==form.cleaned_data.get("password")):
                p = []
                p = ParticipantData.objects.all()
                participants = []
                for j in p:
                    if (j.event_list==(str(i.id)+i.name)):  
                            participants.append(j)
                form = login_form()
                return render(request,"event_detail_view.html",{'participants' : participants}) 
            else:
                form = login_form()
                return render(request,"login_error.html",{})

    return render(request,"login.html",{'form':form})  
