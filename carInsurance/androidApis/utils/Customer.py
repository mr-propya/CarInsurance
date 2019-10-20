from ..models import Customer


def createUser(details):
    customer = Customer()
    print(details["firebaseUid"])
    customer.uid = details["firebaseUid"]
    customer.name = details["name"]
    customer.phoneNum = details["phoneNo"]
    customer.ownedCars = 0
    try:
        customer.save()
    except Exception:
        return {"status": "error"}
    return {"status": "success"}

