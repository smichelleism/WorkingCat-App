from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models

# Create your models here.

class WorkingCatApplication(models.Model):

	#Closed no placement
	#Closed with placement
	#Open Awaiting placement
	#New Contact
	#Pending

	CLOSED 		= 'Closed'
	PLACEMENT	= 'Placement'
	OPEN 		= 'Open'
	PENDING		= 'Pending'
	NEWCONTACT 	= 'NewContact'

	APPLICATION_STATUS_CHOICES = (
		(OPEN, "Open"),
		(CLOSED, "Closed"),
		(PLACEMENT, "Placement"),
		(PENDING, "Pending"),
		(NEWCONTACT, "New Contact")
		)

	application_status 	= models.CharField(max_length = 10, choices = APPLICATION_STATUS_CHOICES, default = NEWCONTACT)
	inventory_loaned	= models.CharField(max_length = 100, blank=True, null=True)
	application_date	= models.DateTimeField(default=timezone.now)
	planned_placement	= models.CharField(verbose_name='What is the planned placment date?', max_length=100, blank=True, null=True)
	first_name          = models.CharField(verbose_name='What is your first name?', max_length=100)
	last_name           = models.CharField(verbose_name='What is your family (last) name?',  max_length=100)
	email               = models.CharField(verbose_name='What is your email?',  max_length=100)
	business_name		= models.CharField(verbose_name='What is your business name?', max_length=100, blank=True, null=True)
	business_type		= models.CharField(verbose_name='What type of business is this? (i.e., winery, stable, private home, etc.', max_length=100, blank=True, null=True)
	street_address  	= models.CharField(verbose_name='What is your street address?',  max_length=200, blank=True, null=True)
	city            	= models.CharField(verbose_name='What is your city?', max_length=50,  blank=True, null=True)
	state           	= models.CharField(verbose_name='What state do you live in?',max_length=2, default="CA", blank=True, null=True)
	zipcode         	= models.CharField(verbose_name='What is your zip code?', max_length=10, blank=True, null=True)
	phone_cell			= models.CharField(verbose_name='What is your cell phone number?',max_length=50, blank=True, null=True)
	phone_land			= models.CharField(verbose_name='What is your home/business telephone number?', max_length=50, blank=True, null=True)
	notes 			    = models.TextField(verbose_name='Describe your need of working cats? ', blank=True, null=True)
	kb_notes			= models.TextField(verbose_name='KB Notes', blank=True, null=True)


	def __str__(self):
		return self.last_name + ', ' + self.first_name



class Cat (models.Model):

	DECEASED 	= 'D'
	ADOPTED 	= 'A'
	PREDATION	= 'P'
	WORKINGCAT 	= 'W'
	UNKNOWN 	= 'U'
	OTHER 		= 'O'


	OUTCOME_CHOICES	= (
		(DECEASED, "Deceased"),
		(PREDATION, "Predation"),
		(ADOPTED, "Adopted"),
		(WORKINGCAT, "Working Cat"),
		(OTHER, "Other"),
		(UNKNOWN, "Unknown")
		)

	TNR			 = 'TNR'
	LAAS 		 = 'LAAS'
	KINDERGARDEN = 'Kindergarden'
	BESTFRIENDS	 = 'Best Friends'


	SOURCE_CHOICES = {
		(TNR, 'TNR'),
		(LAAS, 'LAAS'),
		(KINDERGARDEN, 'Kindergarden'),
		(BESTFRIENDS, 'Best Friends'),
		(UNKNOWN, 'Unknown')
	}

	FEMALE 	= 'F'
	MALE 	= 'M'
	UNKNOWN = 'U'

	GENDER_CHOICES = (
		(FEMALE, "Female"),
		(MALE, "Male"),
		(UNKNOWN, 'Unknown'),
		)

	source 						= models.CharField(max_length = 15, choices=SOURCE_CHOICES, blank=True, null=True, default = UNKNOWN)
	outcome	 					= models.CharField(max_length = 1, choices=OUTCOME_CHOICES, blank=True, null=True)
	outcome_date				= models.DateField(blank=True, null= True)
	name 						= models.CharField(max_length=50, blank=True, null=True)
	description 				= models.CharField(max_length=100,blank=True, null=True)
	gender 						= models.CharField(max_length=1, choices=GENDER_CHOICES, default=UNKNOWN, blank=True, null=True )
	laas_id						= models.CharField(max_length=15, blank=True, null=True)
	pull_date					= models.DateField(blank=True, null=True)
	pull_shelter				= models.CharField(max_length=20, blank=True, null=True)
	pulled_by					= models.CharField(max_length=100, blank=True, null=True)
	microchip_no				= models.CharField(max_length=100, blank=True, null=True)
	microchip_tfx_date			= models.DateField(blank=True, null=True)
	sneuter 					= models.DateField(blank=True, null=True)
	sneuter_location 			= models.CharField(max_length=50,blank=True, null=True)
	notes 						= models.TextField(blank=True, null=True)
	application 				= models.ForeignKey(WorkingCatApplication, blank=True, null=True) 




