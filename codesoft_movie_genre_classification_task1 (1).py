# -*- coding: utf-8 -*-
"""CodeSoft_Movie_Genre_Classification_Task1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11808KtOFcZlkboIEdUl_Jpwdzap2lqXD
"""

import pandas as pd

train=pd.read_csv('/content/fraudTrain.csv')
train.head()

test=pd.read_csv("/content/fraudTest.csv")
test.head()

train.columns

test.columns

print(train.shape)
print(test.shape)

frames = [train,test]
df = pd.concat(frames)
df.shape

df.reset_index(inplace=True)

df.info()

from sklearn.preprocessing import OrdinalEncoder
cols = ['trans_date_trans_time', 'merchant', 'category', 'first', 'last',
        'gender', 'street', 'city', 'state', 'job', 'dob', 'trans_num']
encoder = OrdinalEncoder()
df[cols] = encoder.fit_transform(df[cols])

df.duplicated().sum()

df.isnull().sum()

df['is_fraud'].value_counts()

from sklearn.model_selection import train_test_split
x=df.drop(['is_fraud'],axis=1)
y=df['is_fraud']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)

print(x_train.shape)
print(y_train.shape)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)

from sklearn.metrics import accuracy_score

pred_train = model.predict(x_train)
pred_test  = model.predict(x_test)

print('Training Accuracy : ', accuracy_score(y_train, pred_train))
print('Testing  Accuracy : ', accuracy_score(y_test, pred_test))

from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB()
nb_model.fit(x_train, y_train)

nb_pred_train = nb_model.predict(x_train)
nb_pred_test = nb_model.predict(x_test)

print('Naive Bayes Training Accuracy : ', accuracy_score(y_train, nb_pred_train))
print('Naive Bayes Testing Accuracy : ', accuracy_score(y_test, nb_pred_test))

from sklearn.feature_extraction.text import TfidfVectorizer
text_cols = ['merchant', 'category', 'job']
text_data = df[text_cols].apply(lambda row: ' '.join(row.astype(str)), axis=1)

vectorizer = TfidfVectorizer(max_features=5000)  # You can adjust max_features
tfidf_features = vectorizer.fit_transform(text_data)

from scipy.sparse import hstack

numerical_features = df.drop(columns=['is_fraud'] + text_cols).values
x = hstack([numerical_features, tfidf_features])
y = df['is_fraud']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

model = LogisticRegression()  # Or any other classifier
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
pred_test = model.predict(x_test)

print('Training Accuracy : ', accuracy_score(y_train, pred_train))
print('Testing Accuracy : ', accuracy_score(y_test, pred_test))