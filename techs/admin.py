from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CarModel)
admin.site.register(Yard)
admin.site.register(CarMaker)
admin.site.register(CarsInYard)
