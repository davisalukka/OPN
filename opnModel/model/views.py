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
from .forms import evaluationForm
from .forms import SignUpForm
from .models import *

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"


#Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

#Add this view
class FormPageView(TemplateView):
    template_name = "form.html"

#Add this view
def evaluationform(request):
    #if form is submitted
    if request.method == 'POST':
        #will handle the request later
        form = evaluationForm(request.POST)
        
        if form.is_valid():
            companyName = form.cleaned_data['companyName']
            annualRevenue = form.cleaned_data['annualRevenue']
            yoyGrowth = form.cleaned_data['yoyGrowth'] / 100
            capitalSeeking = form.cleaned_data['capitalSeeking']
            monthlyBurn = form.cleaned_data['monthlyBurn']
            investmentPeriod = form.cleaned_data['investmentPeriod']
            industryMultiplier = form.cleaned_data['industryMultiplier']
            outstandingShares = form.cleaned_data['outstandingShares']
            netincomeatexit =  netIncomeAtExit(float(annualRevenue), float(yoyGrowth), float(investmentPeriod))
            companyvalueatexit = companyValueAtExit(float(netincomeatexit), float(industryMultiplier))
            futurevalue = futureValue(capitalSeeking, yoyGrowth, investmentPeriod)
            requiredownership = requiredOwnership(futurevalue, companyvalueatexit)
            outstandingsharespost = outstandingSharesPost(outstandingShares, futurevalue, companyvalueatexit)
            postmoneyvaluation = postMoneyValuation(companyvalueatexit, yoyGrowth, investmentPeriod)
            premoneyvaluation = preMoneyValuation(postmoneyvaluation, capitalSeeking)
            shareprice = sharePrice(postmoneyvaluation, capitalSeeking)
            requiredrateforprofitability = requiredRateForProfitability(monthlyBurn, annualRevenue)
            #requiredtermforprofitability = requiredTermForProfitabilty(monthlyBurn, annualRevenue, yoyGrowth)
            #revenuegrowth = revenueGrowth(annualRevenue, investmentPeriod, yoyGrowth)
            #projectedsurplus = projectedSurplus(annualRevenue, monthlyBurn, investmentPeriod)
            #confidencelevel = confidenceLevel(investmentPeriod, yoyGrowth, capitalSeeking, annualRevenue)

            return render(request, 'result.html',{
                'companyName': companyName,
                'annualRevenue': annualRevenue,
                'yoyGrowth': yoyGrowth,
                'capitalSeeking': capitalSeeking,
                'monthlyBurn': monthlyBurn,
                'investmentPeriod': investmentPeriod,
                'industryMultiplier': industryMultiplier,
                'outstandingShares': outstandingShares,
                #including evlauated metrics from models.py
                'netIncomeAtExit': netincomeatexit,
                'companyValueAtExit': companyvalueatexit,
                'futureValue': futurevalue,
                'requiredOwnership': requiredownership,
                'outstandingSharesPost': outstandingsharespost,
                'postMoneyValuation': postmoneyvaluation,
                'preMoneyValuation': premoneyvaluation,
                'sharePrice': shareprice,
                'requiredRateForProfitability': requiredrateforprofitability,
                #'requiredTermForProfitabilty': requiredtermforprofitabilty,
                #'revenueGrowth': revenuegrowth,
                #'projectedSurplus': projectedsurplus,
                #'confidenceLevel': confidencelevel,
                })

    else:
        #creating a new form
        form = evaluationForm()
        
    #returning form
    return render(request, 'form.html', {'form':form});

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
        

