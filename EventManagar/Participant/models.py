
# Create your models here.
from asyncio.windows_events import NULL
from django.db import models
from django import forms
# Create your models here.
from django.forms import ValidationError
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField

from Event.models import Eventdata
from django.utils import timezone

# for sms 
from twilio.rest import Client

# for mail 
from django.core.mail import send_mail ,EmailMultiAlternatives
from django.conf import settings

#for error message 

from django.utils.translation import gettext_lazy as _
from django.db.models import CheckConstraint, Q, F # for the conndition From > To

    # creating a list for event_list 
l = []
l =Eventdata.objects.all()
temp_CHOICES = []
for i in l:
    if (i.reg_deadline < timezone.now()):
        continue
    temp_CHOICES.append((str(i.id)+(i.name),(i.name)+" - "+str(i.id)))
CHOICES = tuple(temp_CHOICES)
# Create your models here
class ParticipantData (models.Model):

    name = models.CharField(verbose_name = "Parcipant name", max_length=200)
    contact_no = PhoneNumberField(verbose_name = "Contact No ",help_text="For India start with +91 ")
    email_id = models.EmailField(verbose_name="Enter your Email ID",default="your email address")
    # one way (dangerous)event_list = models.ForeignKey("Event.EventData", verbose_name="Event List", on_delete=models.CASCADE,default=None)
    event_list = models.CharField(max_length=200,choices=CHOICES)
    registration_type = models.CharField(max_length=200,choices=(("Individual","Individual"),("Group","Group")))
    no_of_people = models.IntegerField(verbose_name="No. of people ",default=1)
    # def clean(self):
    #     # Ensures constraint on model level, raises ValidationError
    #     if self.From >= self.To:
    #         # raise error for field
    #         raise ValidationError({'To': _('End date and time  cannot be smaller or equal to start date and time .')})    

    def __str__(self):
        return self.name

    def clean(self):
        flag  =True
         # Ensures constraint on model level, raises ValidationError
        e = self.email_id
        Eventt = self.event_list
        participants = []
        participants =ParticipantData.objects.all()
        for i in participants:
            if (i.email_id==e and i.event_list==Eventt):
            # # raise error for field
            #     flag=False
               raise ValidationError({'event_list': ["This participant have already registered for this Event.If participant wants to register in another event then select another available ",]})
        if (flag):
            #all ok then             
            # mail the host 
            try :
                subject = 'Thank you for using our site for your participant registration.'
                message = 'Thanks for using our website , here are some details \nYour Participant Id :'+ str(self.id) +'\n The Event details:\n' +' Participant name: ' +  self.name+'.\n'+'Contact No. : ' + str( self.contact_no) +'.\n' + 'Email ID : ' + self.email_id +'.\n' +'Event that you participated in:'+self.event_list+'.\n' +'Registration type :'+self.registration_type+'.\n'+'No. of people:'+str(self.no_of_people)+'.\n' 
                email_from = settings.EMAIL_HOST_USER
                recipient_list = []
                recipient_list.append( self.email_id)
                send_mail( subject, message, email_from, recipient_list )  

            except :
                raise ValidationError({'email_id': ["Oops , Something is wrong with your email id , pls enter correct email id",]})    



            # Find your Account SID and Auth Token at twilio.com/console
            # and set the environment variables. See http://twil.io/secure
            account_sid = ''
            auth_token =''
            client = Client(account_sid, auth_token)
            # print(self.contact_no,str(self.contact_no),type(str(self.contact_no)))
            # will be used in twilio sms part
            event = l[0]
            for j in l:
                if (j.name==self.event_list):
                    event=j 
                    print(type(j),type(event))       
            start_date = event.From.strftime("%m/%d/%Y, %H:%M:%S")
            end_date =  event.To.strftime("%m/%d/%Y, %H:%M:%S")
            reg_date =  event.reg_deadline.strftime("%m/%d/%Y, %H:%M:%S")        
            event_detail = ' Your Event name is ' +  event.name+'.\n'+'Event Description: ' +  event.description +'.\n' + ' Your Event\'s poster link is ' + event.link +'.\n' +'Event starting date :'+start_date+'.\n' +'Event ending date :'+end_date+'.\n'+'Event registration deadline :'+reg_date+'.\n' 
            try:
                num_id = str(self.id)
                if (num_id==None):
                    num_id=1
                message = client.messages \
                            .create(
                                body="Your Participant Id : "+ num_id + "\nEvent Details :\n\n" + event_detail,
                                from_='',
                                to= str(self.contact_no)
                            )
                print(message.sid)  
            except:
                raise ValidationError({'contact_no': ["Oops , Something is wrong with your contact no , pls enter correct contact no",]})

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
