from file_upload.forms import DocumentForm
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def file_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'file_upload/file_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'file_upload/file_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') #redirects to this page after success
    else:
        form = DocumentForm()
    return render(request, 'file_upload/model_form_upload.html', {
        'form': form
    })