from django import forms
from .models import Document, Study

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class StudyForm(forms.ModelForm):
    class Meta:
        model=Study
        exclude=['meta_trait_id','observation']