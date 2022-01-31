from django.db import models
from django.forms import ValidationError
from django.urls import reverse

from time import strftime
from django.utils.translation import gettext_lazy as _
from django.db.models import CheckConstraint, Q, F # for the conndition From > To

# for mail 
from django.core.mail import send_mail ,EmailMultiAlternatives
from django.conf import settings

# Create your models here
class Eventdata (models.Model):

    name = models.CharField(verbose_name = "Event name", max_length=200)
    description = models.TextField(verbose_name="Event's description",blank=True)
    link =models.URLField(	verbose_name = "Link of the poster", max_length=10000,blank=True)
    From = models.DateTimeField(verbose_name="From",null =True)
    To= models.DateTimeField(verbose_name="To",null =True)
    reg_deadline = models.DateTimeField(verbose_name="Registration Deadline",null =True)
    host_email =models.EmailField(verbose_name="Host\'s Email ID")
    host_password = models.CharField(verbose_name="Password for event",max_length=33)

    def clean(self):
        # Ensures constraint on model level, raises ValidationError
        if self.From >= self.To :
            # raise error for field
            raise ValidationError({'To': _('End date and time  cannot be smaller or equal to start date and time .')})  
        try:
        #mail the host 
            start_date = self.From.strftime("%m/%d/%Y, %H:%M:%S")
            end_date = self.To.strftime("%m/%d/%Y, %H:%M:%S")
            reg_date =  self.reg_deadline.strftime("%m/%d/%Y, %H:%M:%S")
            subject = 'Thank you for using our site for your Event Registration'
            message = 'It  means a world to us \nThe Event details:\n' +' Your Event name is ' + self.name +'.\n'+'Event Description: ' +  self.description+'.\n' + ' Your Event\'s poster link is ' + self.link+'.\n' +'Event starting date :'+start_date+'.\n' +'Event ending date :'+end_date+'.\n'+'Event registration deadline :'+reg_date+'.\n' +'You can view Participant data for your event on our portal.\n'+'Event Manager app'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = []
            recipient_list.append(self.host_email)
            send_mail( subject, message, email_from, recipient_list )     
        
        except :
            raise ValidationError({'host_email': ["Oops , Something is wrong with your email id , pls enter correct email id",]}) 


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})     


 
