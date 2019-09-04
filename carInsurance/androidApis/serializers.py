from rest_framework import serializers
from .models import FileUpload, Customer


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
