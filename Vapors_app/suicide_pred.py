#!/usr/bin/env python
# coding: utf-8

# Support Vector Machine From Scratch

# Reading Datasets
import numpy as np
import pandas as pd
from django.contrib.staticfiles import finders

path = finders.find("suicide.csv")
students_df = pd.read_csv(path)


# Filtering paramentes
students_df = students_df[["id", "gender", "sexuallity", "age", "bodyweight", "virgin", "prostitution_legal", "pay_for_sex", "friends", "social_fear", "depressed", "attempt_suicide"]]


# Training data
df = students_df[["gender", "sexuallity", "age", "bodyweight", "virgin", "prostitution_legal", "pay_for_sex", "friends", "social_fear", "depressed", "attempt_suicide"]]

# Parameter on which training is done
train_cols = ["gender", "sexuallity", "age", "bodyweight", "virgin", "prostitution_legal", "pay_for_sex", "friends", "social_fear", "depressed"]

# Converting the response variable to -1 for using it in SVM
df['attempt_suicide'][df['attempt_suicide'] == 0] = -1


# Finds closest data of the given class

# Norm of a vector
def norm(w):
    return np.sum(w**2)**0.5

# Euclidian distance
def distance(w, row, b):
    return abs(w.T.dot(row.T) + b)/norm(w)

# Finding closest data of the given class(1 or -1)
def closest_point(w, b, cls):
    dis = float('+inf')
    df_cls = df[df['attempt_suicide']==cls][train_cols]
    for i in range(len(df_cls)):
        if float(distance(w, np.array(df_cls[i:i+1])[0, :], b)) < dis:
            dis = float(distance(w, np.array(df_cls[i:i+1])[0, :], b))
            min_dis = df_cls[i:i+1]
    return min_dis


# Creates random weights from the training datas
def random_wt():
    w = []
    for i in train_cols:
        w.append(np.random.choice(np.array(df[i])))
    return w


# Training SVM(Support Vector Machine)
def svm(lr, b, epochs):
#     Creates random weights for training
    w = pd.DataFrame(random_wt())
#     Lambda
    lamb = 1e-2
    for i in range(epochs):
        # Learning rate for current epoch
        l = lr - (i*lr)/epochs
        
        for j in range(len(df)):
            row = np.array(df[j:j+1])
            if (float((w.T.dot(row[0, :-1].T)+b)*row[0, -1]))<1:
                t = np.array(-lamb*lr*row[0, -1]*row[0, :-1]).reshape((10,1))
                w = np.subtract(w, t)
        
        closest_one = closest_point(w, b, 1)
        closest_minus_one = closest_point(w, b, -1)
        b = -1*(w.T.dot(np.array(closest_one)[0, :]) + w.T.dot(np.array(closest_minus_one)[0, :]))*0.5

    return b, w


# Learning rate
lr = 0.5

# Taking a random intercept
b = np.random.rand()
epochs = 15

# Training SVM on the given data
b, w = svm(lr, b, epochs)

# Intercept after training
print(w)
print("b = "+ str(b))


# ### Testing function
def svm_test(test):
    row = test[0]
    cls = int(np.sign(np.dot(w.T,row[0:].T)+b))
    return cls

# predictng
# pred = svm_test(test = np.array([1, 2, 19, 1, 1, 1, 0, 8.0, 1, 1]).reshape([1, 10]))
# print(pred)