#importing forms
from django import forms

#creating our forms
class SignupForm(forms.Form):
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


