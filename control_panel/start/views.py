from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CamForm, ExtendedUserCreationForm, NotificationsForm, UserUpdateForm
from camera.models import Camera, Image
from django.core.exceptions import ObjectDoesNotExist
from .models import ExtendedUser

from .notifications import notify, notify2
from django.core.paginator import Paginator

def index(request):
    username = request.user.username
    #cameras = Camera.objects.filter(user=request.user)
    context = {'username' : username}
    return render(request, 'start/index.html', context)

@login_required
def profile(request):
    cameralist = Camera.objects.filter(user=request.user.id)
    the_camera = Paginator(cameralist,3)

    grouped_cameras = []
    for page in the_camera.page_range:
        camera_objects = the_camera.page(page).object_list
        grouped_cameras.append(camera_objects)
        
    camera_form = CamForm()
    user_form = UserUpdateForm(instance = request.user)
    try:
        notifications_form = NotificationsForm(instance=request.user.extendeduser)
    except ObjectDoesNotExist:
        ExtendedUser.objects.create(user=request.user)
        notifications_form = NotificationsForm(instance=request.user.extendeduser)

    if request.method =='POST' and 'Save' in request.POST:
        user_form = UserUpdateForm(request.POST, instance = request.user)
        notifications_form = NotificationsForm(request.POST, instance=request.user.extendeduser)
        if user_form.is_valid() and notifications_form.is_valid():
            user_form.save()
            notifications_form.save()
            return redirect('profile')
    elif request.method =='POST' and 'Camera' in request.POST:
        camera_form = CamForm(request.POST)
        if camera_form.is_valid():
            camera = camera_form.save(commit=False)
            camera.user = request.user
            camera.save()
            return redirect('profile')
    elif request.method =='POST' and 'Delete' in request.POST:
        camera_id = request.POST['camera_id']
        try:
            Camera.objects.get(id=camera_id).delete()
        except Camera.DoesNotExist:
            pass
        return redirect('profile')
    
    context = {"u_form" : user_form, "n_form" : notifications_form, "form" : camera_form, 'the_camera' : the_camera, 'grouped_cameras' : grouped_cameras}
    return render(request, 'start/profile.html', context)

@login_required
def archive(request):
    imagelist = []
    cameraList = Camera.objects.filter(user=request.user.id)
    for camera in cameraList:
        image_list = Image.objects.filter(camera=camera.id)
        for img in image_list:
            imagelist.append(img)

    the_image = Paginator(imagelist, 3)

    grouped_images = []
    for page in the_image.page_range:
        image_objects = the_image.page(page).object_list
        grouped_images.append(image_objects)

    context = {'the_image' : the_image, 'grouped_images' : grouped_images}
    return render(request, 'start/archive.html', context)

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()

    context = {'form' : form}
    return render(request, 'start/register.html', context)

def about(request):
        return render(request, 'start/about.html')


def contact(request):
    #temp method for testing functionality
    if request.method == 'POST':
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_msg = request.POST['contact-msg']
        
        return render(request, 'start/contact.html', {'contact_name':contact_name})
        
    else:
        return render(request, 'start/contact.html')
    
#Temporary page for testing functionality    
def testing(request):
    
    if request.method == 'POST':
        
        the_image = Image.objects.get(pk=1)
        
        notify2(request, att=the_image)
        return render(request, 'start/testing.html')
    
    else:    
        the_image = Image.objects.get(pk=1)
        context = {'the_image' : the_image}
        return render(request, 'start/testing.html', context)