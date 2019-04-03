#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from django.contrib.staticfiles import finders

path = finders.find("phq.csv")

# Loading data
names = ("Student_id", "PHQ1A", "PHQ1B", "PHQ1C", "PHQ1D", "PHQ1", "PHQ9", "PHQ6A","PHQ6B", "PHQ6C", "PHQ6D", "PHQ6", "PHQ2A", "PHQ2B", "PHQ2C", "PHQ2", "PHQ3", "PHQ4A", "PHQ4B", "PHQ4C", "PHQ4", "PHQ8", "PHQ5", "PHQ7A", "PHQ7B", "PHQ7C", "PHQ7D", "PHQ7")
# df = pd.read_csv("phq.csv", names=names, skiprows=1)
df = pd.read_csv(path, names=names, skiprows=1)
df.head()


# Separating each PHQ along with its predictor variables
phq1_df = df[["PHQ1A", "PHQ1B", "PHQ1C", "PHQ1D", "PHQ1"]]
phq2_df = df[["PHQ2A", "PHQ2B", "PHQ2C", "PHQ2"]]
phq3_df = df[["PHQ3"]]
phq4_df = df[["PHQ4A", "PHQ4B", "PHQ4C", "PHQ4"]]
phq5_df = df[["PHQ5"]]
phq6_df = df[["PHQ6A","PHQ6B", "PHQ6C", "PHQ6D", "PHQ6"]]
phq7_df = df[["PHQ7A", "PHQ7B", "PHQ7C", "PHQ7D", "PHQ7"]]
phq8_df = df[["PHQ8"]]
phq9_df = df[["PHQ9"]]


phq1_df_train = phq1_df
phq2_df_train = phq2_df
phq3_df_train = phq3_df
phq4_df_train = phq4_df
phq5_df_train = phq5_df
phq6_df_train = phq6_df
phq7_df_train = phq7_df
phq8_df_train = phq8_df
phq9_df_train = phq9_df

rfc1 = RandomForestClassifier(max_depth=2, oob_score=True)
rfc1.fit(phq1_df_train[["PHQ1A", "PHQ1B", "PHQ1C", "PHQ1D"]], phq1_df_train[["PHQ1"]])
rfc2 = RandomForestClassifier(max_depth=2)
rfc2.fit(phq2_df_train[["PHQ2A", "PHQ2B", "PHQ2C"]], phq2_df_train[["PHQ2"]])
rfc4 = RandomForestClassifier(max_depth=2, criterion="entropy")
rfc4.fit(phq4_df_train[["PHQ4A", "PHQ4B", "PHQ4C"]], phq4_df_train[["PHQ4"]])
rfc6 = RandomForestClassifier()
rfc6.fit(phq6_df_train[["PHQ6A","PHQ6B", "PHQ6C", "PHQ6D"]], phq6_df_train[["PHQ6"]])
rfc7 = RandomForestClassifier(max_depth=2, criterion="entropy")
rfc7.fit(phq7_df_train[["PHQ7A","PHQ7B", "PHQ7C", "PHQ7D"]], phq7_df_train[["PHQ7"]])

def phq_preqiction(phq1_df_test, phq2_df_test, phq3_df_test, phq4_df_test, phq5_df_test, phq6_df_test, phq7_df_test, phq8_df_test, phq9_df_test):
    
    # PHQ1
    # Random Forest Classifier for prediciting PHQ1-value
    phq1_val = rfc1.predict(phq1_df_test)
    print("phq1_val: "+ str(phq1_val))


    # PHQ2
    # Random Forest Classifier for prediciting PHQ2-value
    phq2_val = rfc2.predict(phq2_df_test)
    print("phq2_val: "+ str(phq2_val))


    # PHQ3
    phq3_val = np.array(phq3_df_test).reshape(len(phq3_df_test))
    print("\nPHQ3", phq3_val, sep="\n")


    # PHQ4
    # Random Forest Classifier for prediciting PHQ4-value
    phq4_val = rfc4.predict(phq4_df_test)
    print("phq4_val: "+ str(phq4_val))


    # # PHQ5
    # Random Forest Classifier for prediciting PHQ5-value
    phq5_val = np.array(phq5_df_test).reshape(len(phq5_df_test))
    print("\nPHQ5", phq5_val, sep="\n")


    # PH6
    # Random Forest Classifier for prediciting PHQ6-value
    phq6_val = rfc6.predict(phq6_df_test)
    print("phq6_val: "+ str(phq6_val))


    # PHQ7
    # Random Forest Classifier for prediciting PHQ7-value
    phq7_val = rfc7.predict(phq7_df_test)
    print("phq7_val: "+ str(phq7_val))


    # PHQ8
    phq8_val = np.array(phq8_df_test).reshape(len(phq8_df_test))
    print("\nPHQ8", phq8_val, sep="\n")


    # PHQ9
    phq9_val = np.array(phq9_df_test).reshape(len(phq9_df_test))
    print("\nPHQ9", phq9_val, sep="\n")

    # Calculating total PHQ score
    phq = np.sum([phq1_val, phq2_val, phq3_val, phq4_val, phq5_val, phq6_val, phq7_val, phq8_val, phq9_val], axis=0)

    # Classifying as depressed or not based on total PHQ score value based on standard PHQ Score-Depression Severity table
    dep = phq >= 10
    return phq1_val, phq2_val, phq3_val, phq4_val, phq5_val, phq6_val, phq7_val, phq8_val, phq9_val, phq, dep
