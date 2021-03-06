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
    data1=csv.reader(open('act_pred_250_2.csv','rb'))
    user,y_true,y_pred =[],[],[]
    error1 = []
    data1.next()
    user_now = 'Jaya'
    for row in data1: 
        user.append(row[0])
        print user              
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
    print "Average MAE using 250:" 
    print avg1
    print "MAE for 250 ratings"
    print error1

    data2=csv.reader(open('act_pred_500_2.csv','rb'))
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
    print "\nAverage MAE using 500:" 
    print avg2
    print "MAE for 500 ratings"
    print error2 
    
    data3=csv.reader(open('act_pred_800_2.csv','rb'))
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
    print "\nAverage MAE using 800:" 
    print avg3
    print "MAE for 800 ratings"
    print error3 
    

    arr=[1,2,3,4,5,6,7,8,9,10]
    plt.xlabel('Learner')
    plt.ylabel('Mean absolute error')
    plt.title('This graph depicts the MAE for different number of ratings for CF+Onto')
    plt.plot(arr,error1,label='250 ratings')
    plt.plot(arr,error2,label='500 ratings')
    plt.plot(arr,error3,label='800 ratings')
    
    plt.legend()
    plt.show()
    
   
loading()
