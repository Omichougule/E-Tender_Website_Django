from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.contrib.admin.widgets import *


# class DateTimeInput(forms.DateTimeInput):
# 	input_type = 'date'


# Float Tender Form
class TenderForm(ModelForm): 
	class Meta:
		model = Tender
		fields = ['product','description','quantity','startdate','duedate']
		widgets = {
            #'startdate': AdminSplitDateTime(),
			#'duedate': AdminSplitDateTime(),
			'startdate': AdminDateWidget(),
			'duedate': AdminDateWidget(),
		}


# User Registration Form
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


#New Quotation bid Form
class QuotReceivedForm(ModelForm):
	class Meta:
		model = Quotation
		fields = ['tender', 'quotamount']


#
#class QuotStatusChange(ModelForm):
#	class Meta:
#		model = Quotation
#		fields = ['tender', 'quotamount', 'status']
