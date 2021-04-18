from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Structure for Database


class Tender(models.Model):
	STATUS = (
		('Open', 'Open'),
		('Closed', 'Closed'),
		('Awarded', 'Awarded'),
	)
	product = models.CharField(max_length=50, null=True, blank=False)
	description = models.CharField(max_length=200, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=False)
	#startdate = models.DateTimeField(auto_now_add=True, null=True)
	startdate = models.DateTimeField(null=True, blank=False)
	duedate = models.DateTimeField(null=True, blank=False)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	status = models.CharField(max_length=10, null=True, choices=STATUS)

	def __str__(self):
		return str(self.id)

class Quotation(models.Model):
	STATUS = (
		('Open', 'Open'),
		('Closed', 'Closed'),
		('Awarded', 'Awarded'),
	)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
	tender = models.ForeignKey(Tender, on_delete=models.SET_NULL, null=True, blank=False)
	quotamount = models.FloatField(null=True)
	status = models.CharField(max_length=50, null=True, choices=STATUS)


	def __str__(self):
		return str(self.id)

