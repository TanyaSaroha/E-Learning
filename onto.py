# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:24:34 2018

@author: tonio
"""

rows=[]
def loading():
   
        creader =  open('learner_onto.csv','r')
    
        creader.next()
        for row in creader:
           rows.append(row)
            
       
        prefs={}
        for line in rows[:]:
            (user,context,value)=line.split(",")
            prefs.setdefault(user,{})
            prefs[user][context]=float(value)
        
        return prefs
        
from math import sqrt

def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
     if item in prefs[p2]: 
      si[item]=1
    
    n=len(si)
    print n
    if n==0: return 0

    sum1sq=sum([pow(prefs[p1][it],2) for it in prefs[p1]])
    sum2sq=sum([pow(prefs[p2][it],2) for it in prefs[p2]])
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    num = pSum    
    den = sqrt(sum1sq)*sqrt(sum2sq)    
    if den==0: return 0
    
    r=num/den
    
    return r

prefs = loading()
print sim_pearson(prefs,'L1','L2')
print sim_pearson(prefs,'L1','L3')
print sim_pearson(prefs,'L1','L10')
print sim_pearson(prefs,'L1','L20')
print sim_pearson(prefs,'L1','L30')
print sim_pearson(prefs,'L1','L40')
print sim_pearson(prefs,'L1','L50')
print 'Hello'
