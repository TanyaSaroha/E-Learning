# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 05:19:22 2018

@author: killada
"""
import numpy as np

def subtract_elements(a,b):
    diff = []    
    diff = np.subtract(a,b)
    sumx = np.sum(diff)
    print sumx
    accuracyx = sumx/len(diff)    
    return accuracyx
    
rows=[]
from sklearn.metrics import accuracy_score

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
    user,y_true,y_pred =[],[],[]
    #accuracy = []
    data.next()
    #user_now = 'L1'
    #print user_now
    for row in data:        
        user.append(row[0])       
        #print user        
        #l = len(user)
        #print l        
        #print user[l-1]
        #print user_now
        #if user[l-1] == user_now:
        y_true.append(float(row[3]))
        y_pred.append(float(row[2]))
        #else:
        print accuracy_score(y_true,(y_pred>0).astype(int))
            #print list(map(operator.sub, act,pred))
            #acc = act - pred
            #print act
                
            #acc = subtract_elements(act,pred)
            #print acc            
            #accuracy.append(acc)
            #l = len(user)
            #user_now = user[l-1]
        #accuracy = act - pred
    #print accuracy
    #print user
    #print act
    #print pred
