from django.db import models
import math
from .forms import SignupForm
from decimal import Decimal

# Create your models here.
#Declare global variables


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

    #outstandingSharesPre = outStandingShares

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

