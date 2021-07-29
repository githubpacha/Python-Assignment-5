#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 09:37:30 2021

@author: home
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

filename = 'Problem2.csv'
data = pd.read_csv(filename)                #random 20% for test
train_data, test_data = train_test_split(data, test_size=0.2)

#training part
train_x = np.array(train_data[train_data.columns[:-1]])
scl1 = preprocessing.MinMaxScaler().fit(train_x)
train_sclx = scl1.fit_transform(train_x)
train_y = np.array(train_data['Outcome']) #20% outcomes in an array

#testing part
test_x = np.array(test_data[test_data.columns[:-1]])
scl2 = preprocessing.MinMaxScaler().fit(test_x)
test_sclx = scl2.fit_transform(test_x)
test_y = np.array(test_data['Outcome'])



figure, fig1 = plt.subplots(2,2,figsize=(25,25))
figure, fig2 = plt.subplots(3,1,figsize=(25,25))


age = np.array(train_data['Age'])
dpf = np.array(train_data['DiabetesPedigreeFunction'])
glu = np.array(train_data['Glucose'])
ins = np.array(train_data['Insulin'])
bmi = np.array(train_data['BMI'])
bp = np.array(train_data['BloodPressure'])

p_out = np.squeeze(np.where(train_y == 1))
n_out = np.squeeze(np.where(train_y == 0))

lab = ['Diabetic','Not Diabetic']
col = ['r','b']

#Determining by Age
fig1[0][0].hist([age[p_out], age[n_out]], label=lab, color=col)
fig1[0][0].set_title('Determining Diabetes by Age',size=(25))
fig1[0][0].set_xlabel('Age')
fig1[0][0].set_ylabel('Frequency')
fig1[0][0].legend()

#Determining by Diabetes Pedigree Function
fig1[0][1].hist([dpf[p_out], dpf[n_out]], label=lab, color=col)
fig1[0][1].set_title('Determining Diabetes by DPF',size=(25))
fig1[0][1].set_xlabel('Diabetes Pedigree Function')
fig1[0][1].set_ylabel('Frequency')
fig1[0][1].legend()

#Determining by Glucose
fig1[1][0].hist([glu[p_out], glu[n_out]], label=lab, color=col)
fig1[1][0].set_title('Determining Diabetes by Glucose',size=(25))
fig1[1][0].set_xlabel('Glocose')
fig1[1][0].set_ylabel('Frequency')

#Determining by Insulin
fig1[1][1].hist([ins[p_out], ins[n_out]], label=lab, color=col)
fig1[1][1].set_title('Determining Diabetes by Insulin',size=(25))
fig1[1][1].set_xlabel('Insulin')
fig1[1][1].set_ylabel('Frequency')
fig1[1][1].legend()

#Determining by BMI
fig2[0].hist([bmi[p_out], bmi[n_out]], label=lab, color=col)
fig2[0].set_title('Determining Diabetes by BMI',size=(25))
fig2[0].set_xlabel('Body Mass Index')
fig2[0].set_ylabel('Frequency')
fig2[0].legend()

#Determining by Blood Pressure
fig2[1].hist([bp[p_out], bp[n_out]], label=lab, color=col)
fig2[1].set_title('Determining Diabetes by BP',size=(25))
fig2[1].set_xlabel('Blood Pressure')
fig2[1].set_ylabel('Frequency')
fig2[1].legend()

#Accuracy
lgreg = LogisticRegression()
lgreg.fit(train_sclx, train_y)#ready for prediction
accuracy_score = (lgreg.score(test_sclx,test_y))
print('Accuracy: ',accuracy_score*100)

#Correct and Wrong Predictions
prediction = lgreg.predict(test_sclx)
right_pred = np.where(test_y == prediction)
wrong_pred = np.where(test_y != prediction)
fig2[2].scatter(test_x[right_pred, 6], test_x[right_pred, 7],label = 'Right Prediction')
fig2[2].scatter(test_x[wrong_pred, 6], test_x[wrong_pred, 7],label = 'Wrong Prediction')
fig2[2].set_title('Predictions',size=(25))
fig2[2].set_xlabel('Diabetes Pedigree Function')
fig2[2].set_ylabel('Age')
fig2[2].legend()

plt.show()
