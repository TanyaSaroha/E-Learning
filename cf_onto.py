# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 12:41:44 2018

@author: tonio
"""
from math import sqrt

rows=[]
def loading250():
   
        creader =  open('SAMPLE_RATINGS_250.csv','r')
    
        creader.next()
        for row in creader:
           rows.append(row)
            
       
        prefs={}
        for line in rows[:]:
            (user,resource,rating)=line.split(",")
            prefs.setdefault(user,{})
            prefs[user][resource]=float(rating)
            
        return prefs

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
        
def sim_cosine(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
     if item in prefs[p2]: 
      si[item]=1
    
    n=len(si)
    #print n
    if n==0: return 0

    sum1sq=sum([pow(prefs[p1][it],2) for it in prefs[p1]])
    sum2sq=sum([pow(prefs[p2][it],2) for it in prefs[p2]])
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    num = pSum    
    den = sqrt(sum1sq)*sqrt(sum2sq)    
    if den==0: return 0
    
    r=num/den
    
    return r


def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
     if item in prefs[p2]: 
      si[item]=1
    
    n=len(si)
    
    if n==0: return 0
    
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    
    sum1sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2sq=sum([pow(prefs[p2][it],2) for it in si])
    
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1sq-pow(sum1,2)/n)*(sum2sq-pow(sum2,2)/n))
    if den==0: return 0
    
    r=num/den
    
    return r
"""    
def total_sim(sim1=, sim2):
    similarity = sim1 + sim2
    return similarity
"""
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
                    for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getCfRecommendations(pref1s,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs1:
        if other==person: continue
        sim=similarity(prefs1,person,other)
        if sim<=0: continue
        for item in prefs1[other]:
            if item not in prefs1[person] or prefs1[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs1[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    #print rankings
    rankings.sort( )
    rankings.reverse( )
    return rankings

def getOntoRecommendations(pref1s,prefs2, person,similarity1=sim_pearson, similarity2=sim_cosine):
    totals={}
    simSums={}
    for other in prefs1:
        if other==person: continue
        sim1=similarity1(prefs1,person,other)
        sim2=similarity2(prefs2,person,other)
        sim = (sim1+sim2)/2
        if sim<=0: continue
        for item in prefs1[other]:
            if item not in prefs1[person] or prefs1[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs1[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    rankings.sort( )
    rankings.reverse( )
    return rankings

prefs1 = loading250()
prefs2 = loading()
print 'CF'
print getCfRecommendations(prefs1, 'Jaya')
print 'CF + Onto'
print getOntoRecommendations(prefs1, prefs2, 'Jaya')