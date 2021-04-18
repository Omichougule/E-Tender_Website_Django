from django.urls import path
from django.contrib import admin
from . import views

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('received/', views.received, name="received"),
    path('login/', views.login1, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('registerbuyer/', views.registerPagebuyer, name="registerbuyer"),
    path('registerseller/', views.registerPageseller, name="registerseller"),
	path('contactus/', views.contactus, name="contactus"),
	path('aboutus/', views.aboutus, name="aboutus"),
	path('tenderfloat/', views.tenderfloat, name="tenderfloat"),
	path('quotation/', views.quotation, name="quotation"),
	path('updateasclosed/<int:pk>/', views.updateasclosed, name="updateasclosed"),
	path('awarded/', views.awarded, name="awarded"),
	path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
]