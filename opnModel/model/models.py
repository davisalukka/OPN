from django.db import models
import math
#from .forms import evaluationForm
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    #User
    date = models.DateTimeField(auto_now=True)

#Model values calculations

#derivatives
def netIncomeAtExit(annualRevenue, yoyGrowth, investmentPeriod):
    return (annualRevenue * (1 + yoyGrowth)**investmentPeriod)

def companyValueAtExit(netIncomeAtExit, industryMultiplier):
    return(netIncomeAtExit * industryMultiplier)

#Capital Rounds

def futureValue(capitalSeeking, yoyGrowth, investmentPeriod):
    return (capitalSeeking*((1 + yoyGrowth)**(investmentPeriod)))

def requiredOwnership(futureValue, companyValueAtExit):
    return (float(futureValue)/float(companyValueAtExit))

def outstandingSharesPost(outstandingShares, futureValue, companyValueAtExit):
    requiredOwnerShip = requiredOwnership(futureValue, companyValueAtExit)
    return (outstandingShares/(1 - requiredOwnerShip))

def postMoneyValuation(companyValueAtExit, yoyGrowth, investmentPeriod):
    return (companyValueAtExit  /  float(((1+yoyGrowth**(investmentPeriod)))))

def preMoneyValuation(postMoneyValuation, capitalSeeking): 
    return (postMoneyValuation - capitalSeeking)

def sharePrice(postMoneyValuation, outstandingSharesPost):
    return (postMoneyValuation / outstandingSharesPost)

#adjusted Rate Calulation
def requiredRateForProfitability(monthlyBurn, annualRevenue):
    return (((monthlyBurn * 12) - annualRevenue) / annualRevenue)

def requiredTermForProfitability(monthlyBurn, annualRevenue, yoyGrowth):
    return (math.log((MonthlyBurn * 12) / annualRevenue)/(math.log(1 + revenueGrowthYoY)))


"""
#Projected metrics
def revenueGrowth(annualRevenue, investmentPeriod, yoyGrowth):
    currentRevenue = annualRevenue
    Growth = []
    for i in range(investmentPeriod):
        Growth.append(currentRevenue)
        currentRevenue = (currentRevenue * float((1 + yoyGrowth))

    return Growth

def projectedSurplus(annualRevenue, monthlyBurn, investmentPeriod):
    currentRevenue = annualRevenue
    surplusRevenue = currentRevenue - (MonthlyBurn * 12)
    revenueGrowth = []
    for i in range(investmentPeriod):
        revenueGrowth.append(surplusRevenue)
        currentRevenue = currentRevenue * (1 + revenueGrowthYoY)
        surplusRevenue = currentRevenue - (MonthlyBurn * 12)
    return revenueGrowth

#Confidence Level
def confidenceLevel(investmentPeriod, yoyGrowth, capitalSeeking, annualRevenue):
    return ((1 - (investmentPeriod/10))/3+(yoyGrowth/0.5)/3 + (1-(capitalSeeking/annualRevenue))/3)

"""

