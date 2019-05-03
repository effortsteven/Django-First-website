# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

app_name = 'Techs'


# def index(request):
#     return HttpResponse('<h1>my tech page </h1>')

def index(request):
    yards = Yard.objects.all()
    return render(request, 'techs/index.html', {'yards': yards, 'app_title': app_name})


def tech_detail(request, tech_id):
    car = get_object_or_404(CarModel, id=tech_id)
    return render(request, 'techs/tech_details.html', {'car': car, 'app_title': app_name})


def in_stock_cars(request):
    car_models = CarModel.objects.all()
    return render(request, 'techs/cars.html', {'car_models': car_models, 'app_title': 'Cars'})
