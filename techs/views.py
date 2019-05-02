# from django.http import HttpResponse
from django.shortcuts import render

app_name = 'tech'


# def index(request):
#     return HttpResponse('<h1>my tech page </h1>')

def index(request):
    return render(request, 'techs/index.html')
