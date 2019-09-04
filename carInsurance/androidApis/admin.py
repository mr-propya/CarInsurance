from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.Car)
admin.site.register(models.Insurance)
admin.site.register(models.Claims)
admin.site.register(models.Predictions)
admin.site.register(models.Transactions)


# Register your models here.
