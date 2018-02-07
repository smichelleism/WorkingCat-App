from django import forms
from .models import WorkingCatApplication

class WorkingCatApplicationModelForm(forms.ModelForm):
	class Meta:
		model = WorkingCatApplication
		fields = (
			'first_name', 
			'last_name', 
			'email')