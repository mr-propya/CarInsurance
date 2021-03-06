from ..models import Car, Transactions
from ..models import Insurance as InsuranceModel
from django.forms.models import model_to_dict


class Insurance:
    def newInsurance(self, data):
        res = dict()
        car = Car.objects.filter(vehicleNum=data["vehicle"]).first()
        if car is None:
            res["status"] = "error"
            res["error"] = "This car is not registered"
        else:
            insurance = InsuranceModel()
            insurance.car = car
            from django.utils import timezone
            insurance.dateOfInsurance = timezone.now()
            insurance.monthlyPremium = float(data["monthly"])
            insurance.balance = 0.0
            insurance.save()
            res["status"] = "success"
        return res


    def payAmount(self, data):
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

    def getExistingInsuarance(self,data):
        res = dict()
        car = Car.objects.filter(vehicleNum=data["vehicle"]).first()
        if car is None:
            res["status"] = "error"
            res["error"] = "This car is not registered"
            return res
        insurance = InsuranceModel.objects.filter(car=car).first()
        if insurance is None:
            res["status"] = "error"
            res["error"] = "This car has no active insurances"
            return res
        print(insurance)
        res["status"] = "success"
        res["insurance"]=model_to_dict(insurance)
        return res