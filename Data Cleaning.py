# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:01:19 2020

@author: jider
"""

import pandas as pd

df= pd.read_csv('vehicles.csv')

df.columns

df.describe

#To remove duplicate rows

df.drop_duplicates(inplace = True)

#Check for null values and % of null values

df.isnull()

#Using the 'any' method to check for null for each column:
    
    df.isnull().any()
    
df.isnull().sum()/df.shape[0]

#Remove null columns over a particular threshold

thresh = len(df)*.6

df.dropna(thresh= thresh, axis= 1)

df.dropna(thresh= thresh, axis= 1).shape
df.dropna(thresh= 21, axis = 0).shape

#Inputing null values

df.odometer.fillna(df.odometer.median())

df.odometer.fillna(df.odometer.median()).isnull().any()
df.odometer.fillna(df.odometer.mean()).isnull().any()

# To convert everything here to all lower or upper

df.description.head()
df.description.head().apply(lambda x: x.lower())

#For the above .ending with head() showed "float has no attribute lower". 
#Moving from float to str is easier, str to float is a little complicated

#Float to string

df.description.astype(str).apply(lambda x: x.lower())

df.dtypes

#To calculate the length of the text

df['text_len']= df.description.apply(lambda x: len(str(x)))

(df['text_len'].value_counts() > 1).sum()

#Converting from float

df.cylinders.head()

---# To know the data type..It is a mixed type/object

     df.cylinders.dtype

---#To change to numerical types

     df.cylinders.value_counts()
     
df.cylinders= df.cylinders.apply(lambda x: str(x).lower().replace('cylinders','').strip())

---#To see the distribution
    df.cylinders.value_counts()

---#To convert "others" category to Nan. That is, invalid parsing sets to NaN

    df.cylinders= pd.to_numeric(df.cylinders, errors= 'coerce')
    df.cylinders.value_counts()
    
---#To be sure both NaNs add up 
    df.cylinders.isnull().sum()
    
----//Histograms & Boxplot\\------

df.boxplot('price')

df.boxplot('odometer')

df.hist('price')

df.price.max()

df.odometer.max()

# Skewness observed/extreme values found. To clean, outliers are to be removed

-----#For the numeric variables:
     
numeric = df._get_numeric_data()

#Inport the modules

#Import the modules

from scipy import stats
import numpy as np

#Taken that there are no null values

df_outliers= df[(df.price< df.price.quantile(.995)) & (df.price > df.price.quantile(.005))]

df_outliers.boxplot('price')

df_outliers.hist('price')

df_outliers= df[(df.odometer< df.odometer.quantile(.995)) & (df.odometer > df.odometer.quantile(.005))]

df_outliers.boxplot('odometer')

df_outliers.hist('odometer')

-----//Scaling\\----

#Using min-max scaling, we need a new library i.e. sklearn

from sklearn.preprocessing import MinMaxScaler

----# Create the scaler object

     Scaler = MinMaxScaler()

----#Fit the object and apply to the dataset

Scaler.fit(df.cylinders.values.reshape(-1,1))

-----#As is often the case with sklearn MLAs, I transform the new inputs after fitting the model

      Scaler.transform(df.cylinders.values.reshape(-1,1))

# Otherwise, I can combine both fit and tranform
 
      Scaler.fit_transform(df.cylinders.values.reshape(-1,1))


        
        
        
        
























    









    
    
    
    