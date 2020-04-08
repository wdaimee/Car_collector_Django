from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello Cars!</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    success_url = '/cats/'

class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

