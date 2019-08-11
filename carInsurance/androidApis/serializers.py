from rest_framework import serializers
from .models import FileUpload

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"
