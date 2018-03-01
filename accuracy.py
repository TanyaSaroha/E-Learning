# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 05:19:22 2018

@author: killada
"""
import numpy as np
import matplotlib.pyplot as plt
rows=[]
from sklearn.metrics import mean_absolute_error

def loading():
    import csv
    data1=csv.reader(open('act_pred150.csv','rb'))
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
            error1.append(mean_absolute_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error1.append(mean_absolute_error(y_true,y_pred))
    avg1=np.sum(error1)/10
    print "Average MAE using 150:" 
    print avg1
    print "MAE for 150 ratings"
    print error1
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
    avg2=np.sum(error)/10
    print "\nAverage MAE using 200:" 
    print avg2
    print "MAE for 200 ratings"
    print error 
    data2=csv.reader(open('act_pred_250.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error2 = []
    data2.next()
    user_now = 'L1'
    for row in data2: 
       
        user.append(row[0])              
        l = len(user)
        if user[l-1] == user_now:
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
        else:
            error2.append(mean_absolute_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error2.append(mean_absolute_error(y_true,y_pred))
    avg3=np.sum(error2)/10
    print "\nAverage MAE using 250:" 
    print avg3
    print "MAE for 250 ratings"
    print error2 
    arr=[1,2,3,4,5,6,7,8,9,10]
    plt.xlabel('Learner')
    plt.ylabel('Mean absolute error')
    plt.title('This graph depicts the MAE for different number of ratings')
    plt.plot(arr,error1,label='150 ratings')
    plt.plot(arr,error,label='200 ratings')
    plt.plot(arr,error2,label='250 ratings')
    plt.legend()
    plt.show()
    
   
