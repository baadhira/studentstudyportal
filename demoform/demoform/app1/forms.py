from django import forms
from app1.models import student
class studentform(forms.ModelForm):   #Form definition
    class Meta:
        model=student
        fields='__all__'