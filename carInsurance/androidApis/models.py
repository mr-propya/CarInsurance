from django.db import models


class FileUpload(models.Model):
    uploadedFile = models.FileField()

    def __str__(self):
        return self.uploadedFile.name


class Customer(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=15)
    ownedCars = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    vehicleNum = models.CharField(max_length=20)
    purchasedAt = models.DateTimeField(blank=True)
    model = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicleNum
