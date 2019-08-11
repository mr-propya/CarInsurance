from django.db import models

# Create your models here.


class FileUpload(models.Model):
    uploadedFile = models.FileField()

    def __str__(self):
        return self.uploadedFile.name
