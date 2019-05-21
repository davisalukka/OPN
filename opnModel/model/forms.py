#importing forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import valuationMetrics

#Evaluation form
class valuationMetricsForm(forms.ModelForm):

    class Meta:

	
	
        model = valuationMetrics
        fields = ['companyName','annualRevenue','yoyGrowth','capitalSeeking','monthlyBurn','investmentPeriod','industryMultiplier','outstandingShares','industryVertical']
        labels = {
                'companyName': 'Company Name',
                'annualRevenue': 'Annual Revenue',
                'yoyGrowth': 'Yoy Growth',
                'capitalSeeking': 'Capital Seeking: ',
                'monthlyBurn': 'Monthly Burn: ',
                'investmentPeriod': 'Investment term length: ',
                'industryMultiplier': 'Standard Industry Multiplier:',
                'outstandingShares': 'Outstanding Shares: ',
                'industryVertical': 'Industry Vertical',
                }
        standardMultipliers = ((1,5),(2,10),(3,15),(4,20),(5,25))
        input_type = {
                'industryMultiplier': forms.ChoiceField(choices=standardMultipliers),
                }



    

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=100, required=False, help_text = 'Required.')
    first_name = forms.CharField(max_length=100, required=False, help_text = 'Optional.')
    last_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    company_name = forms.CharField(max_length=100, required=False, help_text='Required.')
    email=forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','company_name', 'email', 'password1', 'password2',)


