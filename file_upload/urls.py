from django.urls import path
from . import views

urlpatterns=[
    path('',views.file_upload, name='file_upload'),
    path('study/',views.meta_form, name='study_upload'),
]