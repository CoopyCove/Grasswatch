from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('archive/',views.archive, name='archive'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
]