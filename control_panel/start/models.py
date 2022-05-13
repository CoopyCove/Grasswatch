from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.
class ExtendedUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SMS_notifications = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=12,default='000-000-0000')
    latest_notify = models.DateField(default = timezone.now, null=True)
    
    notification_interval = models.CharField(
        max_length = 11,
        default = 'weekly',
        choices = [('immediate','Immediately'),('daily','Daily'),('weekly','Weekly')] 
    )


    def __str__(self):
        return str(self.user)