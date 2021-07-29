#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:32:32 2021

@author: home
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:48:33 2021

@author: home
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


filename = 'Problem1.txt' 
data = pd.read_csv(filename, delimiter='\t')
train_data, test_data = train_test_split(data, test_size=0.1)


train_x = train_data[train_data.columns[-4:]]
test_x = test_data[test_data.columns[-4:]]

scl1 = preprocessing.MinMaxScaler().fit(train_x)
scl2 = preprocessing.MinMaxScaler().fit(test_x)

train_sclx = scl1.fit_transform(train_x)
train_y = np.array(train_data['fruit_label'])

test_sclx = scl2.fit_transform(test_x)
test_y = np.array(test_data['fruit_label'])

knn = KNeighborsClassifier( n_neighbors=5 )
knn.fit(train_sclx, train_y)

knn_pred = knn.predict(test_sclx)
knn_acc = (metrics.accuracy_score(test_y, knn_pred))

lgreg = LogisticRegression()
lgreg.fit(train_sclx, train_y)

lgreg_pred = lgreg.predict(test_sclx)
lgreg_acc = (lgreg.score(test_sclx, test_y))

print("K-Nearest Neighbour accuracy:",knn_acc*100)
print("Logistic Regression accuracy:",lgreg_acc*100)
if knn_acc > lgreg_acc:
    print("K-Nearest Neighbour is better Logistic Regression.")
elif knn_acc < lgreg_acc:
    print("Logistic Regression is better K-Nearest Neighbour.")
else:
    print("Indetereminant of the both.")

#plotting figures
figure, sub = plt.subplots(2,2)
figure.set_size_inches(25, 20)

sub[0][0].hist(train_y, 4, width=0.5)
label = ['Apple', 'Mandarin', 'Orange', 'Lemon']
rct = sub[0][0].patches
for i, j in zip(rct, label):
    h = i.get_height()
    sub[0][0].text((i.get_x() + i.get_width()/2), h+0.01, j, ha='center', va='bottom')
sub[0][0].set_title('Fruits Distribution by their Frequency',size=(25))
sub[0][0].set_xlabel('Fruits')
sub[0][0].set_ylabel('Frequency')

grps = train_data.groupby('fruit_name')
for naam,grp in grps:
    sub[0][1].plot(grp['width'], grp['height'],marker='o',linestyle='',label = naam)
sub[0][1].set_title('Fruits Distribution by Height on Weight',size=(25))
sub[0][1].set_xlabel('Width')
sub[0][1].set_ylabel('Height')
sub[0][1].legend()

#K-Nearest Neighbour Algorithm Prediction Plot
p_knn_pred = np.where(test_y == knn_pred)
n_knn_pred = np.where(test_y != knn_pred)
sub[1][0].scatter(test_sclx[p_knn_pred,1],test_sclx[p_knn_pred,2],label='Right Prediction')
sub[1][0].scatter(test_sclx[n_knn_pred,1],test_sclx[n_knn_pred,2],label='Wrong Prediction')
sub[1][0].set_title('K-Nearest Neighbour Algorithm Prediction',size=(25))
sub[1][0].set_xlabel('Width')
sub[1][0].set_ylabel('Height')
sub[1][0].legend()

#Logistic Regression  Algorithm Prediction Plot
p_lgreg_pred = np.where(test_y == lgreg_pred)
n_lgreg_pred = np.where(test_y != lgreg_pred)
sub[1][1].scatter(test_sclx[p_lgreg_pred,1],test_sclx[p_lgreg_pred,2],label='Right Prediction')
sub[1][1].scatter(test_sclx[n_lgreg_pred,1],test_sclx[n_lgreg_pred,2],label='Wrong Prediction')
sub[1][1].set_title('Logistic Regression  Algorithm Prediction',size=(25))
sub[1][1].set_xlabel('Width')
sub[1][1].set_ylabel('Height')
sub[1][1].legend()

plt.show()