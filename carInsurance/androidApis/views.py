from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.http.response import HttpResponse
from .serializers import FileSerializer
from .getPredictions import predict
from .utils import Insurance
from .utils.Customer import Customer
from .utils.Car import Car
from django.views.decorators.csrf import  csrf_exempt

# Create your views here.
class BaseApiView(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def getResults(self, req, function):
        res = function(req.data)
        print(res)
        return JsonResponse(res,safe=False)


def index(req):
    predict("")
    return HttpResponse("It works")


class GetResult(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def post(self,req):
        response = dict()
        response["status"] = "success"
        file = FileSerializer(data=req.data)
        if file.is_valid():
            file.save()
            print(file.data["uploadedFile"])
            response["predictions"] = predict(file.data["uploadedFile"])
            response["file"] = file.data["uploadedFile"]
        else:
            response["status"] = "failed"
            response["error"] = "file format not supported or invalid"

        return Response(response)


class getCars(BaseApiView):
    def post(self,req):
        return super().getResults(req,Customer().getCars)


class verifyUser(BaseApiView):
    def post(self,req):
        return super().getResults(req,Customer().verifyUser)

class addUser(BaseApiView):

    def post(self, req):
        return super().getResults(req,Customer().createUser)


class addCarForUser(BaseApiView):

    def post(self, req):
        return super().getResults(req,Car().newCar)


class buyInsurance(BaseApiView):

    def post(self, req):
        return super().getResults(req,Insurance.newInsurance)


class payAmount(BaseApiView):
    def post(self, req):
        return super().getResults(req, Insurance.payAmount)

class getInsurance(BaseApiView):
    def post(self,req):
        return super().getResults(req,Insurance.Insurance().getExistingInsuarance)