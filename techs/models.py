from django.db import models


# Create your models here.
class CarMaker(models.Model):
    makerName = models.CharField(max_length=100)
    makerOwner = models.CharField(max_length=200)
    makerLogo = models.ImageField(upload_to="car_maker/")

    def __str__(self):
        return self.makerName


class CarModel(models.Model):
    modelName = models.CharField(max_length=100)
    modelYear = models.IntegerField()
    modelOwner = models.CharField(max_length=100)
    modelMaker = models.ForeignKey(CarMaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.modelName


class Yard(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    yardName = models.CharField(max_length=100)
    yardPhone = models.IntegerField()

    def __str__(self):
        return self.yardName


class CarsInYard(models.Model):
    NameOfYard = models.ForeignKey(Yard, on_delete=models.CASCADE)
    carName = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.NameOfYard.yardName
