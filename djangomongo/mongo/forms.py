from django import forms
from .models import MongoTestModel


class MongoForm(forms.ModelForm):

    class Meta:
        model = MongoTestModel
        fields = "__all__"
        
       

