# Django automatically import admin module in the 'main' app as we have added "django.contrib.admin" in our setting.py.(in settings.py)
# This function attempts to import an admin module in each installed application.(in settings.py)
# Such modules are expected to register models with the admin.models is the python file where we have all our model classes. 


from django.contrib import admin
from .models import *              # We are importing all the classes using '*' symbol to register those classes in our admin panel

# Register your models here.
# Here we register all the model classes in our admin panel

admin.site.register(Tender)
admin.site.register(Quotation)