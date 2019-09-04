from .models import Customer, Car

class CustomerHelper:
    def createUser(self, details):
        customer = Customer()
        print(details["firebaseUid"])
        customer.uid = details["firebaseUid"]
        customer.name = details["name"]
        customer.phoneNum = details["phoneNo"]
        customer.ownedCars = 0
        customer.save()


class CarHelper:
    def newCar(self, details):
        car = Car()
        car.model = details["model"]
        car.purchasedAt = details["timePurchased"]
        car.vehicleNum = details["registrationNum"]
        car.save()


    def sellCar(self,carId):
        Car.objects.get(pk=carId).delete()