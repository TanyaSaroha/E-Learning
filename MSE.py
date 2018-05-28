# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:13:29 2018

@author: tonio
"""

import numpy as np
import matplotlib.pyplot as plt
rows=[]
from sklearn.metrics import mean_squared_error

def loading():
    import csv
    data1=csv.reader(open('act_pred_model2.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error1 = []
    data1.next()
    user_now = 'L1'
    for row in data1: 
       
        user.append(row[0])              
        l = len(user)
        if user[l-1] == user_now:
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
        else:
            error1.append(mean_squared_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error1.append(mean_squared_error(y_true,y_pred))
    avg1=np.sum(error1)/10
    print "Average MSE for model 2" 
    print avg1
    print "MSE for model 2"
    print error1
    data=csv.reader(open('act_pred_250.csv','rb'))
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
            error.append(mean_squared_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error.append(mean_squared_error(y_true,y_pred))
    avg2=np.sum(error)/10
    print "\nAverage MSE for model1" 
    print avg2
    print "MSE for model1"
    print error 
    arr=[1,2,3,4,5,6,7,8,9,10]
    plt.xlabel('Learner')
    plt.ylabel('Mean Squared error')
    plt.title('This graph depicts the MSE for different models')
    plt.plot(arr,error1,label='CF+onto')
    plt.plot(arr,error,label='CF')
    #plt.plot(arr,error2,label='250 ratings')
    plt.legend()
    plt.show()
    
   
loading()