from django import forms


class FileUpload(forms.Form):
    fileCheck = forms.FileField()
    message = forms.CharField(max_length=50)
