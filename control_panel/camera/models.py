from django.db import models
from django.contrib.auth.models import User

camtypes =(
    ('wyze','WYZE'),
    ('sonoff', 'SONOFF'),
)

class Camera(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 50)
    rtsp_url = models.URLField(default = '')
    camera = models.CharField(max_length=10, choices=camtypes, default='wyze')

    def __str__(self):
        return self.name

class Image(models.Model):
    camera = models.ForeignKey(Camera, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    image = models.ImageField(null=True)
    results = models.CharField(max_length = 100, null = True, blank = True)
    date = models.DateTimeField(null=True)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.name