# from django.http import HttpResponse
from django.shortcuts import render
from .models import *

app_name = 'tech'


# def index(request):
#     return HttpResponse('<h1>my tech page </h1>')

def index(request):
    car_models = CarModel.objects.all()
    return render(request, 'techs/index.html', {'car_models': car_models})
