from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.response import Response
from django.http.response import HttpResponse
from .serializers import FileSerializer
from .getPredictions import predict
from .utils import Customer, Car, Insurance


# Create your views here.
class BaseApiView(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def getResults(self, req, function):
        res = function(req.data)
        print(res)
        return Response(str(res))



def index(req):
    predict("")
    return HttpResponse("It works")


class GetResult(APIView):
    parser_classes = [JSONParser,MultiPartParser]

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

        return Response(response)


class addUser(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, req):
        data = req.data
        res = Customer.createUser(details=data)
        return Response(str(res))


class addCarForUser(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, req):
        data = req.data
        res = Car.newCar(details=data)
        print(res)
        return Response(str(res))


class buyInsurance(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def post(self, req):
        res = Insurance.newInsurance(req.data)
        print(res)
        return Response(str(res))

#
# class payAmount(APIView):
#     parser_classes = [JSONParser, MultiPartParser]
#
#     def post(self, req):
#         res = Insurance.payAmount(req.data)
#         print(res)
#         return Response(str(res))




class payAmount(BaseApiView):
    def post(self, req):
        return super().getResults(req, Insurance.payAmount)

