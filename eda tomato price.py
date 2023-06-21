# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:06:41 2023

@author: MRUTYUNJAY
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r'D:\Downloads\Tomato.csv')
df.sample(10)
df.drop(['Unit','Market'],inplace=True,axis=1)
df.sample(2)
df.Date.isnull().sum()
df.dtypes
df['Date']=pd.to_datetime(df['Date'])
df['year']=df['Date'].dt.year
df.year.sample(5)
df['monthno']=df['Date'].dt.month
df.monthno.sample(5)
date=df.Date
df.drop(['Date'],axis=1)
date.head(2)
sns.boxplot(x='year',y='Average',data=df)
sns.violinplot(x='year',y='Average',data=df)
sns.heatmap(df.pivot_table(values='Average',index='year',columns='monthno'))
sns.scatterplot(x='monthno',y='Minimum',hue='Maximum',data=df)
sns.clustermap(pd.crosstab(df['Average'],df['year']))
sns.relplot(data=df,kind="line",x="monthno",y="Minimum",facet_kws=dict(sharex=False))
plt.hist(df['Minimum'],density=True,histtype='bar')
sns.relplot(data=df,kind="line",x="monthno",y="Maximum",facet_kws=dict(sharex=False))
plt.hist(df['Maximum'],density=True,histtype='bar')
plt.plot(df.monthno,df.Minimum,'b-x',linewidth=4,markersize=12,markeredgewidth=4,markeredgecolor='navy')
plt.plot(df.monthno,df.Maximum,'r--o',linewidth=4,markersize=12);
plt.title('Prices variation through out the year')
plt.legend(['Minimum','Maximum'])
plt.xlabel('Month');plt.ylabel('Price')
plt.title("Distribution of Average prices")
sns.distplot(df.Average,bins=5);
print(df.Average.skew())
df.Average.describe()
Mean of Average prices is 38.185516