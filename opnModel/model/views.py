from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
#from model.tokens import account_activation_token
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from .forms import valuationMetricsForm
from .models import *
import model
# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"


#Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

#Add this view
class FormPageView(TemplateView):
    template_name = "form.html"

def evaluationFormView(request):
	if  request.method == 'POST':
			form = valuationMetricsForm(request.POST)
			if(form.is_valid()):
				valuationMetrics = form.save(commit = False)
				valuationMetrics.user = request.user
				valuationMetrics.save()
				metrics = model.models.valuationMetrics.objects.get(user=request.user)
				context = {'form': form, 'metrics': metrics }
				return render(request, "evaluation_form.html", context)
			
	form = valuationMetricsForm()
	try:
		metrics = model.models.valuationMetrics.objects.get(user=request.user)
		context = {'form': form, 'metrics': metrics }
	except:
		context = {'form': form	}

	return render(request, "evaluation_form.html", context)


	


def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() #Load the profile instance created by the signal. 
            user.profile.company_name = form.cleaned_data.get('company_name')
            user.save()
            username=form.cleaned_data['username']
            raw_password=form.cleaned_data['password1']
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html',{'form':form})
        

