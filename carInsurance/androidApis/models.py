from django.db import models


class FileUpload(models.Model):
    uploadedFile = models.FileField()

    def __str__(self):
        return self.uploadedFile.name


class Customer(models.Model):
    uid = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=15)
    ownedCars = models.IntegerField()


class Car(models.Model):
    vehicleNum = models.CharField(max_length=20)
    purchasedAt = models.DateTimeField(blank=True)
    model = models.CharField(max_length=50)
    owner = models.ForeignKey(Customer,on_delete=models.CASCADE())


class Insurance(models.Model):
    dateOfInsurance = models.DateField()
    monthlyPremium = models.FloatField()
    balance = models.FloatField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE())


class Claims(models.Model):
    verified = models.BooleanField()
    raisedAt = models.DateTimeField()
    settledAt = models.DateTimeField()
    price = models.IntegerField()
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE())


class Predictions(models.Model):
    predictedAt = models.DateTimeField()
    predictedPrice = models.IntegerField()
    actualPrice = models.IntegerField()
    claim = models.ForeignKey(Claims, on_delete=models.CASCADE())


class Transactions(models.Model):
    time = models.TimeField()
    transactionId = models.IntegerField()
    status = models.CharField(max_length=20)
    car = models.ForeignKey(Car,on_delete=models.CASCADE())
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE())

