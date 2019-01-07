#importing forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import valuationMetrics

#creating our forms
class evaluationForm(forms.Form): #instead of forms.Form
    #Company name. 
    companyName = forms.CharField(label="Company name", max_length=100)
    #Annual revenue
    annualRevenue = forms.FloatField(label="Annual revenue")
    #Year on year growth rate
    yoyGrowth = forms.DecimalField(label="Yoy growth in decimal")
    #Amount of capital being requested
    capitalSeeking = forms.IntegerField(label="Capital being requested")
    #Monthly capital expense
    monthlyBurn = forms.IntegerField(label="Monthly burn")
    #Investment term length
    investmentPeriod = forms.IntegerField(label="Investment term length")
    #Standard industry multipliers
    standardMultipliers = ((1,5),(2,10),(3,15),(4,20),(5,25))
    industryMultiplier = forms.ChoiceField(label="P/E Ratio",choices=standardMultipliers)   
    #Outstanding shares before investment
    outstandingShares = forms.IntegerField(label="Outstanding shares")

class valuationMetricsForm(forms.ModelForm):
    class Meta:
        model = valuationMetrics
        exclude = []
        labels = {
                'companyName': 'Company Name',
                'annualRevenue': 'Annual Revenue',
                'yoyGrowth': 'Yoy Growth',
                'capitalSeeking': 'Capital Seeking: ',
                'monthlyBurn': 'Monthly Burn: ',
                'investmentPeriod': 'Investment term length: ',
                'industryMultiplier': 'Standard Industry Multiplier:',
                'outstandingShares': 'Outstanding Shares: ',
                }
        standardMultipliers = ((1,5),(2,10),(3,15),(4,20),(5,25))
        input_type = {
                'industryMultiplier': forms.ChoiceField(choices=standardMultipliers),
                }



    

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=100, required=False, help_text = 'Optional.')
    first_name = forms.CharField(max_length=100, required=False, help_text = 'Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    company_name = forms.CharField(max_length=100, required=False, help_text='Required.')
    email=forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','company_name', 'email', 'password1', 'password2',)


