from ..models import Customer as CustomerModel
from django.forms.models import model_to_dict

class Customer:

    def verifyUser(self, details):
        username = details["username"]
        password = details["password"]
        response = { 'status':'success' }
        users = CustomerModel.objects.filter(username=username,password = password).get()
        import json
        if users == None:
            response['result'] = 'invalid credentials'
        else:
            response['result'] = 'loggedIn'
            response['user'] = model_to_dict(users)
            print(model_to_dict(users))
        return response

    def addCar(self,details):
        pass

    def createUser(self,details):
        customer = CustomerModel()
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

