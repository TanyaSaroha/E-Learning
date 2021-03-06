# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt

rows=[]
def loading():
   
        creader =  open('ratings_250.csv','r')
    
        creader.next()
        for row in creader:
           rows.append(row)
            
       
        prefs={}
        for line in rows[:]:
            (user,resource,rating)=line.split(",")
            prefs.setdefault(user,{})
            prefs[user][resource]=float(rating)
            
        return prefs
        
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
def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
                    for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other==person: continue
        sim=similarity(prefs,person,other)
        if sim<=0: continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    sub = list()
    rating = list()
        
    rankings.sort( )
    rankings.reverse( )
    print rankings
    for it in rankings:
        a,b = it
        sub.append(a)
        rating.append(b)
    return [sub,rating]

prefs = loading()
user = str(input('Enter User'))
print 'Recommendations:'
getRecommendations(prefs, user)
#sub = list()
#rating = list()
#sub,rating = getRecommendations(prefs, user)
#print sub
#print rating
#print prefs[user]
