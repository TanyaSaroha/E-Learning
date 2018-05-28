# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:18:45 2018

@author: tonio
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
from math import sqrt

def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})
            result[item][person]=prefs[person][item]
    return result

def sim_distance(prefs,person1,person2):
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    if len(si)==0: return 0

    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
                    for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def calculateSimilarItems(prefs,n=10):
    result={}
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
        c+=1
        if c%100==0: print "%d / %d" % (c,len(itemPrefs))
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        result[item]=scores
    #for item in result:
        #print item
        #print result[item]
    return result

def getRecommendedItems(prefs,itemMatch,user):
    userRatings=prefs[user]
    scores={}
    totalSim={}
    for (item,rating) in userRatings.items( ):
        for (similarity,item2) in itemMatch[item]:
            if item2 in userRatings: continue

            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating

            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity

    rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
    rankings.sort( )
    rankings.reverse( )   
    return rankings

prefs = loading250()
user = input('Enter User')
#print sim_pearson(prefs,'L1','L2')
#print topMatches(prefs,user)
#print getRecommendations(prefs, user)
#print prefs[user]
print 'Hello'
itemsim = calculateSimilarItems(prefs,n=10)
#print itemsim
#itemsim2 = calculateSimilarItems(prefs,n=5)
#print itemsim2
print getRecommendedItems(prefs,itemsim, user)
#print getRecommendedItems(prefs,itemsim2, user)