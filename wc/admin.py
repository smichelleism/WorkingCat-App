from django.contrib import admin
from .models import WorkingCatApplication, Cat
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.

class CatInlineTab(admin.TabularInline):
	model = Cat
	extra = 0
	formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'10'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
    }


@admin.register(WorkingCatApplication)
class TNRApplicationAdmin(admin.ModelAdmin):
	list_display = ('application_status', 'planned_placement', 'application_date', 'first_name', 'last_name', 'business_name', 'business_type', 'city')
	list_filter = ['application_status']
	search_fields = [ 'first_name', 'last_name']
	inlines = [CatInlineTab, ]

@admin.register(Cat)
class Cat(admin.ModelAdmin):
	search_fields = ['name', 'laas_id', 'microchip_no']
	list_filter = ['outcome', 'source']
	list_display = ('outcome', 'outcome_date', 'source', 'name', 'description', 'gender', 'laas_id')