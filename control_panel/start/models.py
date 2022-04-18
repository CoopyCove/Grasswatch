from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    SMS_notifications = models.BooleanField(default=True)
    email_notifications = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=12,default='000-000-0000')

    def __str__(self):
        return str(self.user)