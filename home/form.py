from .models import *
from froala_editor.widgets import FroalaEditor
from django import forms

class Blog_form(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['content',]