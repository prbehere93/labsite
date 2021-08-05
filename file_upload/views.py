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
            uploaded_file=request.FILES['document']
            file_ext=uploaded_file.name.split('.')[-1]
            print(file_ext)
            if file_ext=='csv':
                print('something')
            #print(form.fields['description'], form.fields['document']) the uploaded fields of the form in the form of an object

            form.save()
            return redirect('home') #redirects to this page after success
    else:
        form = DocumentForm()
    return render(request, 'file_upload/model_form_upload.html', {
        'form': form
    })