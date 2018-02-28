# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 05:19:22 2018

@author: killada
"""
import matplotlib.pyplot as plt
rows=[]
from sklearn.metrics import mean_absolute_error

def loading():
    import csv
    data=csv.reader(open('act_pred.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error = []
    data.next()
    user_now = 'L1'
    for row in data: 
       
        user.append(row[0])              
        l = len(user)
        if user[l-1] == user_now:
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
        else:
            error.append(mean_absolute_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error.append(mean_absolute_error(y_true,y_pred))
    print error 
    arr=[1,2,3,4,5,6,7,8,9,10]
    plt.plot(arr,error)
    plt.show()
   
