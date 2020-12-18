from django import forms
from . models import Note
from ckeditor.widgets import CKEditorWidget

class Noteform (forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
        fields = ['title','content','tags']


    
