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
    data1=csv.reader(open('act_pred_800.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error1 = []
    data1.next()
    user_now = 'Jaya'
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
    print "Average MAE for model 1 - CF" 
    print avg1
    print "MAE for model 1 - CF"
    print error1
    
    data2=csv.reader(open('act_pred_800_2.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error2 = []
    data2.next()
    user_now = 'Jaya'
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
    avg2=np.sum(error2)/10
    print "\nAverage MAE for model2 - CF + Onto" 
    print avg2
    print "MAE for model2 - CF + Onto"
    print error2
    
    data3=csv.reader(open('act_pred_800_3.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error3 = []
    data3.next()
    user_now = 'Jaya'
    for row in data3: 
        user.append(row[0])              
        l = len(user)
        if user[l-1] == user_now:
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
        else:
            error3.append(mean_absolute_error(y_true,y_pred))
            y_true,y_pred =[],[]
            y_true.append(float(row[3]))
            y_pred.append(float(row[2]))
            l = len(user)
            user_now = user[l-1]
    error3.append(mean_absolute_error(y_true,y_pred))
    avg3=np.sum(error3)/10
    print "\nAverage MAE for model3 - CF + Onto + MF" 
    print avg3
    print "MAE for model3 - CF + Onto + MF"
    print error3
    

    arr=[1,2,3,4,5,6,7,8,9,10]
    plt.xlabel('Learners')
    plt.ylabel('Mean Absolute error')
    plt.title('This graph depicts the MAE for different models')
    plt.plot(arr,error1,label='CF')
    plt.plot(arr,error2,label='CF + Onto')
    plt.plot(arr,error3,label='CF + Onto + MF')
    
    plt.legend()
    plt.show()
    
   
loading()
