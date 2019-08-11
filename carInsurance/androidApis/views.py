from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import FileSerializer

# Create your views here.


class GetResult(APIView):
    parser_classes = [JSONParser,MultiPartParser]

    def post(self,req):
        response = dict()
        response["status"] = "success"
        file = FileSerializer(data=req.data)
        if file.is_valid():
            file.save()
            print(file.data["uploadedFile"])
            response["file"] = file.data["uploadedFile"]
        else:
            response["status"] = "failed"
        return Response(response)


@csrf_exempt
def inbuilt(req):
    print(type(req.files))
    return HttpResponse("hi there")
