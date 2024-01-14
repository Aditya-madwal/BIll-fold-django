from django import forms
from .models import *

class transactions_form(forms.ModelForm):
    class Meta:
        model = transactions
        fields = '__all__'
