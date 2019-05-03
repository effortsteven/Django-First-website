from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tech/car_detail_<tech_id>/', views.tech_detail, name='tech_detail'),
    path('cars/', views.in_stock_cars, name='in_stock_cars')

]