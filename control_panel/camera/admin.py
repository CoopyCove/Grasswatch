from django.contrib import admin
from .models import Camera
from .models import Image

admin.site.register(Camera)
admin.site.register(Image)
