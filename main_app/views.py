from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Car:
    def __init__(self, make, model, year, color, description):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.description = description

cars = [
    Car('Ferrari', 'F40', 1987, 'Red', 'Greatest Italian car ever made'),
    Car('McLaren', 'F1', 1991, 'Black', 'The pinnacle of Engineering'),
    Car('Acura', 'NSX', 1992, 'Yellow', 'What all super cars should be like')
]

def home(request):
    return HttpResponse('<h1>Hello Cars!</h1>')

def about(request):
    return render(request, 'about.html')

def car_index(request):
    return render(request, 'cars/index.html', {'cars': cars})