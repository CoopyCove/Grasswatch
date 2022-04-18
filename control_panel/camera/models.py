from django.db import models
from django.contrib.auth.models import User

class Camera(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 50)
    rtsp_url = models.URLField(default = '')

    def __str__(self):
        return self.name

class Image(models.Model):
    camera = models.ForeignKey(Camera, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    image = models.ImageField(null=True)
    results = models.CharField(max_length = 100, null = True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name