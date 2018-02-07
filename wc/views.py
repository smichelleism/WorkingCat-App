from django.shortcuts import render, redirect
from django import forms
from .forms import WorkingCatApplicationModelForm
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.

@xframe_options_exempt
def application_upload(request):
	if request.method == "POST":
		form = WorkingCatApplicationModelForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('https://kittybungalow.org/home-school-application-thank-you/')
	else:
		form = WorkingCatApplicationModelForm()

	return render(request, "application.html", {'form':form})