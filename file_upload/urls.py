from django.urls import path
from . import views

urlpatterns=[
    path('',views.file_upload, name='file_upload'),
    path('model_file/',views.model_form_upload, name='model_file_upload'),
]