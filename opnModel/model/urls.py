#model/urls.py
from django.conf.urls import url
from model import views
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView 

urlpatterns = [
        path('',TemplateView.as_view(template_name='home.html'), name='home'),
        path('about/', views.AboutPageView.as_view(), name='about'), #Add this /about/ route
        path('form/', views.evaluationFormView, name='form'), #Add this /form/ view
        #path('signup/', views.signup, name='signup'), #add the signup and registration view
        path('admin/', admin.site.urls, name='admin'),#add the admin view
        path('accounts/', include('accounts.urls')),
        path('accounts/', include('django.contrib.auth.urls')), #new
        ]
