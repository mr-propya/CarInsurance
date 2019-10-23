from ..models import Customer, Car


class Car:

    def newCar(self, details):
        car = Car()
        response = {}
        response["status"] = "success"
        if details["uid"] == None:
            response["status"] = "error"
            response["error"] = "no UID provided"
            return response
        user = Customer.objects.filter(uid = details["uid"]).first()
        if user == None:
            response["status"] = "error"
            response["error"] = "no user found"
            return response
        car.model = details["model"]
        import datetime
        car.purchasedAt = datetime.datetime(int(details["YY"]),
                                            int(details["MM"]),
                                            int(details["DD"]))
        car.vehicleNum = details["registrationNum"]
        car.owner = user
        car.save()
        return response

    def sellCar(self, carId):
        Car.objects.get(pk=carId).delete()

