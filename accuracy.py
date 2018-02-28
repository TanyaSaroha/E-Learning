# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 05:19:22 2018

@author: killada
"""
def subtract_lists(a,b):
    for i, val in enumerate(a):
        val = val-b[i]
    return a
    
rows=[]
def loading():
   
        #creader =  open('act_pred.csv','r')
       # import pandas as pd
       # df=pd.read_csv('act_pred.csv')
        
       # saved_column=df.actual
       # print saved_column
    
        #creader.next()
        #for row in creader:
           #rows.append(row)
            
       
       # prefs={}
       # for line in rows[:]:
            #(user,resource,pred,actual)=line.split(",")
           # prefs.setdefault(user,{})
           # prefs[user][resource]=float(pred),float(actual)
            
       # return prefs
    import csv
    data=csv.reader(open('act_pred.csv','rb'))
    user,act,pred =[],[],[]
    accuracy = []
    data.next()
    user_now = 'L1'
    #print user_now
    for row in data:        
        user.append(row[0])       
        #print user        
        l = len(user)
        #print user[l-1]
        print user_now
        if user[l-1] == user_now:
            act.append(float(row[3]))
            pred.append(float(row[2]))
        else:
            #print list(map(operator.sub, act,pred))
            #acc = act - pred
            #print act
            acc = subtract_lists(act,pred)
            accuracy.append(acc)
            l = len(user)
            user_now = user[l-1]
        #accuracy = act - pred
        print accuracy
    #print user
    #print act
    #print pred
