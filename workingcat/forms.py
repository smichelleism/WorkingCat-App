from django import forms
from .models import WorkingCatApplication

class WorkingCatApplicationModelForm(forms.ModelForm):
    class Meta:
        model = WorkingCatApplication
        fields = (
            'first_name', 
            'last_name', 
            'email',
            'business_name',
            'business_type',
            'street_address',
            'city',
            'state',
            'zipcode',
            'phone_cell',
            'phone_land',
            'notes',
            )