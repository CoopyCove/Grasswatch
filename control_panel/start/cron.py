from operator import truediv
from camera.models import Image
#from predition_single import predict
from .notifications import notify
import datetime


def predictImages():
    images = Image.objects.filter(results__isnull=True)
    for img in images:
        img.results = "70%" #<------ predict function from prediction_single.py
        img.save(update_fields=['results'])
        User = img.camera.user
        if  User.extendeduser.notification_interval == 'immediate':
            sendNotify(User, img)

def notifyUsers():
    images = Image.objects.exclude(results__isnull=True).filter(notified=False)
    for img in images:
        User = img.camera.user
        if checkUserPreference(User):
            sendNotify(User, img)

def sendNotify(User,img):
    User.extendeduser.latest_notify = datetime.date.today()
    User.extendeduser.save(update_fields=['latest_notify'])
    notify(User, att= img)
    img.notified = True
    img.save(update_fields=['notified'])

def checkUserPreference(User):
    notification_interval = User.extendeduser.notification_interval
    time_difference = datetime.date.today() - User.extendeduser.latest_notify
    if notification_interval == 'daily' and time_difference.days >= 1:
        return True
    elif notification_interval == 'weekly' and time_difference.days >= 7:
        return True
    return False
