# -*- coding: utf-8 -*-
"""CodeSoft_spam_Task4

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1z7uECxA864VoKuDaDCDEa9zcG1b46ABh
"""

nltk.download('stopwords')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix, roc_curve, roc_auc_score
import nltk
from nltk.corpus import stopwords
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Try reading the file with 'latin-1' encoding
df = pd.read_csv('/content/spam.csv', encoding='latin-1')
# If 'latin-1' doesn't work, try other encodings like 'iso-8859-1', 'cp1252', etc.

df.head()

# Build an AI model that can classify SMS messages as spam or
# legitimate. Use techniques like TF-IDF or word embeddings with
# classifiers like Naive Bayes, Logistic Regression, or Support Vector
# Machines to identify spam messages

# Data preprocessing
df = df[['v1', 'v2']]
df.rename(columns={'v1': 'label', 'v2': 'message'}, inplace=True)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF vectorization
tfidf = TfidfVectorizer()
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Model training (Logistic Regression)
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Model evaluation
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, y_pred))

df.info()

from sklearn.svm import SVC

# Model training (SVM)
svm_model = SVC(kernel='linear')  # You can experiment with different kernels
svm_model.fit(X_train_tfidf, y_train)

# Model evaluation (SVM)
svm_y_pred = svm_model.predict(X_test_tfidf)
svm_accuracy = accuracy_score(y_test, svm_y_pred)
print(f"\nSVM Accuracy: {svm_accuracy}")
print(classification_report(y_test, svm_y_pred))

from sklearn.naive_bayes import MultinomialNB

# Model training (Naive Bayes)
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)

# Model evaluation (Naive Bayes)
nb_y_pred = nb_model.predict(X_test_tfidf)
nb_accuracy = accuracy_score(y_test, nb_y_pred)
print(f"\nNaive Bayes Accuracy: {nb_accuracy}")
print(classification_report(y_test, nb_y_pred))