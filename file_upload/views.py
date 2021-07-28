from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def file_upload(request):
    return render(request, 'file_upload/file_upload.html')