from django import forms
from app1.models import Vihicle

class VihicleForm(forms.ModelForm):

    class Meta:
        model=Vihicle

        fields='__all__'