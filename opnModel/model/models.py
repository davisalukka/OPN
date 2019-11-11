from django.db import models
import math
#from .forms import evaluationForm
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import decimal
import feedparser
from simple_history.models import HistoricalRecords

# Create your models here.
#Declare global variables

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date=models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()



class valuationMetrics(models.Model):


     
    user = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    #Company name. 
    companyName = models.CharField(max_length=100)
    #Annual revenue
    annualRevenue = models.IntegerField()
    #Year on year growth rate
    yoyGrowth =  models.DecimalField(max_digits=5,decimal_places=3)
    #Amount of capital being requested
    capitalSeeking =  models.IntegerField()
    #Monthly capital expense
    monthlyBurn = models.IntegerField()
    #Investment term length
    investmentPeriod = models.IntegerField()
    #Standard industry multipliers
    standardMultipliers = ((1,5),(2,10),(3,15),(4,20),(5,25))
    industryMultiplier = models.IntegerField(choices=standardMultipliers)
    #Outstanding shares before investment
    outstandingShares = models.IntegerField()
    #Industry vertical
    industryVertical = models.CharField(max_length=150, default="")
    #User
    date = models.DateTimeField(auto_now=True)
    #History
    history = HistoricalRecords()
    
    @property
    def netIncomeAtExit(self):
         value = (self.annualRevenue * (( 1 + (self.yoyGrowth/(decimal.Decimal(100)))) ** self.investmentPeriod))
         decimal.Decimal(value)
         output = round(value, 2)
         return output

    def feeds(self):

        myFeeds = list()
        industryVertical = self.industryVertical.replace(' ','+')
        try:
            feeds = feedparser.parse('https://news.google.ca/news/feeds?pz=1&cf=all&ned=en&hl=ca&q='+industryVertical+'&output=rss')
            for i in range(25):
                myFeeds.append(feeds.entries[i])
            return myFeeds

        except Exception as e:
            return myFeeds
    


    def companyValueAtExit(self):
         return(self.netIncomeAtExit * self.industryMultiplier)

    def futureValue(self):
         value =  (self.capitalSeeking * ((1 + (self.yoyGrowth/(decimal.Decimal(100)))) ** self.investmentPeriod))
         decimal.Decimal(value)
         output = round(value, 2)
         return output

    def requiredOwnership(self):
         value = (self.futureValue() / self.companyValueAtExit())
         output = round(value, 2)
         return output

    def outstandingSharesPost(self):
         value1 = self.requiredOwnership()
         value2 = (self.outstandingShares / (1 - value1))
         output = round(value2, 2)
         return output

    def postMoneyValuation(self):
        value1 = decimal.Decimal(( (1 + (self.yoyGrowth / (decimal.Decimal(100)))) ** self.investmentPeriod))
        value = self.companyValueAtExit() / value1
        output = round(value, 2)
        return output
 
    def preMoneyValuation(self):
        value = self.postMoneyValuation() - self.capitalSeeking
        output = round(value, 2)
        return output

    def sharePrice(self):
        value = self.postMoneyValuation() / self.outstandingSharesPost()
        output = round(value, 2)
        return output

    def requiredRateForProfitability(self):
        value = (((self.monthlyBurn * 12) - self.annualRevenue) / self.annualRevenue)
        output = round(value, 2)
        return output

    def requiredTermForProfitability(self):
        value1 = math.log((self.monthlyBurn * 12) / self.annualRevenue)
        value2 = math.log(1 + self.yoyGrowth)
        value = value1 / value2
        output = round(value, 2)
        return output
	
    def revenueGrowth(self):
        currentRevenue = self.annualRevenue
        Growth = []
        for i in range(self.investmentPeriod):
              Growth.append(currentRevenue)
              currentRevenue = round((currentRevenue * float((1 + (self.yoyGrowth / decimal.Decimal(100))))),2)
        return Growth
 
    def projectedSurplus(self):
        currentRevenue = self.annualRevenue
        surplusRevenue = currentRevenue - (self.monthlyBurn * 12)
        revenueGrowth = []
        for i in range(self.investmentPeriod):
              revenueGrowth.append(round(float(surplusRevenue),2))
              currentRevenue = currentRevenue * (1 + (self.yoyGrowth / decimal.Decimal(100)))
              surplusRevenue = currentRevenue - (self.monthlyBurn * 12)
        return revenueGrowth

    def confidenceLevel(self):
        value1 = (self.investmentPeriod / decimal.Decimal(10)) / 30
        value2 = (self.yoyGrowth / 30)
        value3 = (self.capitalSeeking / self.annualRevenue) / 40
        output = round(decimal.Decimal(value1) + decimal.Decimal(value2) + decimal.Decimal(value3), 2)
        return output

