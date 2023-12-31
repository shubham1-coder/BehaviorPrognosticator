# -*- coding: utf-8 -*-
"""prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lQ-Kzq4Qf50WleVTdkZ6r0KgMnu2qgF2
"""



import pickle
with open('knn_model.pickle','rb') as f:
  knn_new = pickle.load(f)

with open('scaler.pickle','rb') as f:
  scaler_new = pickle.load(f)

import pandas as pd
new_df = pd.read_csv("https://raw.githubusercontent.com/futurexskill/projects/main/knn-classification/new_customers.csv")

new_df

gender_encoded_new = pd.get_dummies(new_df['Gender'], drop_first=True)

gender_encoded_new

df_new_2 = pd.concat([new_df,gender_encoded_new],axis=1)

df_new_2

x_new = df_new_2[['Male','Age','Salary','Price']].to_numpy()

x_new

x_new_scale2 = scaler_new.fit_transform(x_new)

x_new_scale2

y_new_pred = knn_new.predict(x_new_scale2)

y_new_pred

df_new_2['will_purchase'] = y_new_pred

df_new_2

df_new_2.to_csv("model_predictions.csv",index=False)

import pickle

with open('knn_model_prediction.pickle','wb') as f:
  pickle.dump(knn_new,f)