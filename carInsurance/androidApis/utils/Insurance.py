from ..models import Insurance, Car, Transactions


def newInsurance(data):
    res = dict()
    car = Car.objects.filter(vehicleNum=data["vehicle"]).first()
    if car is None:
        res["status"] = "error"
        res["error"] = "This car is not registered"
    else:
        insurance = Insurance()
        insurance.car = car
        from django.utils import timezone
        insurance.dateOfInsurance = timezone.now()
        insurance.monthlyPremium = float(data["monthly"])
        insurance.balance = 0.0
        insurance.save()
        res["status"] = "success"
    return res


def payAmount(data):
    res = dict()
    car = Car.objects.filter(vehicleNum=data["vehicle"]).first()
    if car is None:
        res["status"] = "error"
        res["error"] = "This car is not registered"
        return res
    insurance = Insurance.objects.get(car=car)
    if insurance is None:
        res["status"] = "error"
        res["error"] = "This car has no active insurances"
        return res
    print(insurance)
    trans = Transactions()
    from django.utils import timezone
    trans.time = timezone.now()
    trans.insurance = insurance
    res["status"] = "success"
    return res