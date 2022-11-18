import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Importing the required libraries.


from sklearn.cluster import KMeans, k_means #For clustering
from sklearn.decomposition import PCA #Linear Dimensionality reduction.


df = pd.read_csv("sales_data_sample.csv",encoding='Latin-1') #Loading the dataset.

df.shape()

df.head()


df.describe()

df.isnull()

df.isnull().sum()

df.info()

df.dtypes

df_drop  = ['ADDRESSLINE1', 'ADDRESSLINE2', 'STATUS','POSTALCODE', 'CITY', 'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME', 'CUSTOMERNAME', 'ORDERNUMBER']
df = df.drop(df_drop, axis=1) #Dropping the categorical uneccessary columns along with columns having null values. Can't fill the null values are there are alot of null values.

df.isnull().sum()

df.dtypes

df['COUNTRY'].unique()

df['PRODUCTLINE'].unique()


df['DEALSIZE'].unique()

productline = pd.get_dummies(df['PRODUCTLINE']) #Converting the categorical columns.
Dealsize = pd.get_dummies(df['DEALSIZE'])

df = pd.concat([df,productline,Dealsize], axis = 1)
df_drop  = ['COUNTRY','PRODUCTLINE','DEALSIZE'] #Dropping Country too as there are alot of countries.
df = df.drop(df_drop, axis=1)
df['PRODUCTCODE'] = pd.Categorical(df['PRODUCTCODE']).codes #Converting the datatype.df.drop('ORDERDATE', axis=1, inplace=True) #Dropping the Orderdate as Month is already included.df.dtypes #All the datatypes are converted into numeric