from file_upload.forms import DocumentForm, StudyForm
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
import numpy as np
import regex as re
import csv
import io

def file_upload(request):
    def process_data(data):
        #creating a empty dataframe to store the processed values
        data_processed=pd.DataFrame(columns=['Accession no','Variable','Biological Rep','Technical Rep','Value'])
        
        #regex to identify the columns with values (bio + tech reps)
        reps=data.filter(regex='b\d').columns
        reps=[i.split('_') for i in list(reps)]
        
        #small lambda func to separate the int from the string and then sort the string on the basis of the int
        biological_reps=sorted(list(set([i[0] for i in reps])), key=lambda key:int([i for i in re.split('([0-9]+)', key)][1]))
        technical_reps=sorted(list(set([i[1] for i in reps])), key=lambda key:int([i for i in re.split('([0-9]+)', key)][1]))
        accessions=data['Accession no.'].unique()
        variables=data['Variable'].unique()
        
        #storing the count of the unique elements of each col
        len_accessions=len(accessions)
        len_variables=len(variables)
        len_biological_reps=len(biological_reps)
        len_technical_reps=len(technical_reps)
        rows=len_accessions*len_variables*len_biological_reps*len_technical_reps
        
        #create individual lists for each of the columns and then fit them into the created dataframe (the order of the created lists is very important)
        technical_rep_list=np.tile(technical_reps,(len_accessions*len_variables*len_biological_reps))
        biological_rep_list=np.tile(np.repeat(biological_reps,len(technical_reps)),(len_accessions*len_variables))
        variables_list=np.repeat(variables,(len_accessions*len_biological_reps*len_technical_reps))
        accessions_list=np.repeat(accessions,(len_variables*len_biological_reps*len_technical_reps))
        #storing the values as a list too (will need to recheck if the information is being parsed correctly)
        #it's esentially creating a transpose of each of the values row and then appending it to an array i.e. then used to create a df
        values_list=np.array([])
        for i in range(0,data.shape[0]):
            values_list=np.append(values_list,data.filter(regex='b\d').iloc[i])
        
        #filling the columns of the final df
        data_processed['Accession no']=accessions_list
        data_processed['Variable']=variables_list
        data_processed['Biological Rep']=biological_rep_list
        data_processed['Technical Rep']=technical_rep_list
        data_processed['Value']=values_list
        
        return(data_processed)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file=request.FILES['document']
            file_ext=uploaded_file.name.split('.')[-1]
            #print(file_ext)
            if file_ext=='csv':
                file=uploaded_file.read().decode('utf-8') #reads from inmemoryupload
                reader=csv.DictReader(io.StringIO(file))
                data = [line for line in reader]
                uploaded_file=pd.DataFrame(data)
                uploaded_file=process_data(uploaded_file)
                print(type(uploaded_file), uploaded_file.columns) #the uploaded file is the modified csv file
                form.save()
            else:
                #show an error message
                print("Does nothing right now")
            return redirect('home') #redirects to this page after success
    else:
        form = DocumentForm()
    return render(request, 'file_upload/file_upload.html', {
        'form': form
    })


def meta_form(request):
    if request.method=='POST':
        form=StudyForm(request.POST)
        if form.is_valid():
            return redirect('home')
        else:
            form=StudyForm()
    else:
        form=StudyForm()
    return render (request, 'file_upload/meta_upload.html', {'form':form})