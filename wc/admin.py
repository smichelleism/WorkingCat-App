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
	list_display = ('application_status', 'application_date', 'planned_placement', 'first_name', 'last_name', 'business_name', 'business_type', 'city')
	list_filter = ['application_status']
	search_fields = [ 'first_name', 'last_name']
	inlines = [CatInlineTab, ]

@admin.register(Cat)
class Cat(admin.ModelAdmin):
	search_fields = ['name', 'laas_id', 'microchip_no']
	list_filter = ['outcome', 'source']
	list_display = ('source', 'laas_id', 'pull_date', 'outcome', 'outcome_date', 'name' )