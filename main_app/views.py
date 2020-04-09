from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .models import *
from .forms import MaintenanceForm
# Create your views here.

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'carcollector123'

def home(request):
    return HttpResponse('<h1>Hello Cars!</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    parts_car_doesnt_have = Part.objects.exclude(id__in = car.parts.all().values_list('id'))
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', 
    {'car': car, 'maintenance_form': maintenance_form, 'parts': parts_car_doesnt_have}
    )

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cats/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

def add_maint(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.car_id = car_id
        new_maint.save()
    return redirect('detail', car_id=car_id)

class PartList(ListView):
    model = Part

class PartDetail(DetailView):
    model = Part

class PartCreate(CreateView):
    model = Part
    fields = '__all__'

class PartUpdate(UpdateView):
    model = Part
    fields = '__all__'

class PartDelete(DeleteView):
    model = Part
    success_url = '/parts/'

def assoc_part(request, car_id, part_id):
  Car.objects.get(id=car_id).parts.add(part_id)
  return redirect('detail', car_id=car_id)

def add_photo(request, car_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.')]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except Exception as e:
            print(e)
            print('An error occurred uploading file to s3')
    return redirect('detail', car_id=car_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # create a form with all the request data
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm() #if the form is not valid, empty the contents of the form
    context = {'form': form, 'error_message': error_message} # initialize contex
    return render(request, 'registration/signup.html', context) # return the user to the registration page

