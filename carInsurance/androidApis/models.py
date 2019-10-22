from django.db import models


class FileUpload(models.Model):
    uploadedFile = models.FileField()

    def __str__(self):
        return self.uploadedFile.name


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=15)
    ownedCars = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    vehicleNum = models.CharField(max_length=20)
    purchasedAt = models.DateTimeField(blank=True)
    model = models.CharField(max_length=50)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, default="User")

    def __str__(self):
        return self.vehicleNum


class Insurance(models.Model):
    dateOfInsurance = models.DateField()
    monthlyPremium = models.FloatField()
    balance = models.FloatField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, default="Insurance")


class Claims(models.Model):
    verified = models.BooleanField()
    raisedAt = models.DateTimeField()
    settledAt = models.DateTimeField()
    price = models.FloatField()
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)


class Predictions(models.Model):
    predictedAt = models.DateTimeField()
    predictedPrice = models.FloatField()
    actualPrice = models.FloatField()
    claim = models.ForeignKey(Claims, on_delete=models.CASCADE, default="Predictions")


class Transactions(models.Model):
    time = models.TimeField()
    transactionId = models.IntegerField()
    premiumId = models.IntegerField()
    status = models.CharField(max_length=20)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, default="Transactions")
