from django.db import models
from django_extensions.db.models import TimeStampedModel

# Create your models here.
class Document(TimeStampedModel):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/') #is uploaded to media_root/documents
