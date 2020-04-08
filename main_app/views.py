from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import MaintenanceForm
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
    maintenance_form = MaintenanceForm()
    return render(request, 'cars/detail.html', {'car': car, 'maintenance_form': maintenance_form})

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

def add_maint(request, car_id):
    form = MaintenanceForm(request.POST)
    if form.is_valid():
        new_maint = form.save(commit=False)
        new_maint.car_id = car_id
        new_maint.save()
    return redirect('detail', car_id=car_id)



