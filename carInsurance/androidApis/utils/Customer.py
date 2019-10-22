from ..models import Customer


class Customer:
    def createUser(details):
        customer = Customer()
        print(details["firebaseUid"])
        customer.username = details["userName"]
        customer.name = details["name"]
        customer.phoneNum = details["phoneNo"]
        customer.ownedCars = 0
        try:
            customer.save()
        except Exception:
            return {"status": "error"}
        return {"status": "success"}

