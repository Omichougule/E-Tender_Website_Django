from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
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
	path('tenderprocess/', views.tenderprocess, name="tenderprocess"),
	path('tenderfloat/', views.tenderfloat, name="tenderfloat"),
	path('quotation/', views.quotation, name="quotation"),
	path('updateasclosed/<int:pk>/', views.updateasclosed, name="updateasclosed"),
	path('awarded/', views.awarded, name="awarded"),

	# Admin date calender
	path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),  

	# Password Reset
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"), name="reset_password"),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
	path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name="password_reset_confirm"),
	path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),

]