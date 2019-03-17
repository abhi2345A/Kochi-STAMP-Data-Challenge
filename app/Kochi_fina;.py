#!/usr/bin/env python
# coding: utf-8

# In[375]:


import numpy as np
import pandas as pd
import seaborn as sns
import json
from pprint import pprint
import matplotlib.pyplot as plt
from IPython.display import HTML, display
#get_ipython().run_line_magic('matplotlib', 'inline')


# #################################################

# In[ ]:


metr = pd.read_csv('final-data/Data_Set_Final_Hack/Mobility/Kochi Metro/KMRL Ticketing Data/KMRL_Historic_Ticketing_Data.csv')


# In[385]:


metr['Transaction Time'] = pd.to_datetime(metr['Transaction Time'],infer_datetime_format=True)
metrr = metr.groupby([metr['Transaction Time'].dt.date]).size()
df19  = metr[metr['Date']=='19-06-2017']
dfmon  = metr[metr['Date']=='20-06-2017']
dfTue = metr[metr['Date']=='21-06-2017']
dfWed  = metr[metr['Date']=='22-06-2017']
dfThurs  = metr[metr['Date']=='23-06-2017']
dfFri  = metr[metr['Date']=='24-06-2017']
dfsat  = metr[metr['Date']=='25-06-2017']
dfsun  = metr[metr['Date']=='26-06-2017']


# In[409]:


def PlotCount(df19):
    grouper = pd.TimeGrouper(freq="30T")
    df19.index = df19.reset_index()['Transaction Time'].apply(lambda x: x - pd.Timestamp(x.date()))
    df19count = df19.groupby(grouper).count()

    df19count.drop(columns=['Station','Equipment Type','Equipment ID','Fare Media','Fare Product','Ticket/Card Number','Transaction Type','Date','Time'],inplace=True)

    df19count['newcolumn'] = df19count.index

    plt.figure(figsize=(10,10))

    df19count['Transaction Time'].plot(kind='barh')
    plt.savefig('books_read.png')
    
    
    df19count['newcolumn'] = pd.to_datetime(df19count['newcolumn'])
    df19count.rename(columns={'Transaction Time':'Count'},inplace=True)
    df19count.reset_index(inplace=True)

    datetimee = '20-03-2019 21:10'
    datetimee = pd.to_datetime(datetimee)

    def Rushcounter(datetimee):
        (time,count)=(0,0)
        for y in df19count.index:
            if df19count.iloc[y,2].hour==datetimee.hour:
                if df19count.iloc[y,2].minute<=datetimee.minute:
                    (time,count)=(df19count.iloc[y,0],df19count.iloc[y,1])
        return time,count
    
    def RushIndicator(datetimee):
        time,count = Rushcounter(datetimee)
        describe = df19count.describe()
        minn = describe['Count']['min']
        maxx = describe['Count']['max']
        average = describe['Count']['mean']
        low  = minn
        h    = maxx
        m    = average
        l1   = (minn+average)/2
        h1   = (average+maxx)/2

        if count>=low and count<l1:
            print('Rush is Low')
        elif count>=l1 and count<m:
            print('Rush is Moderate')
        elif count>=m and count<h1:
            print('Rush is High')
        elif count>=h1 and count<h:
            print('Rush is Very High')
        
        
    RushIndicator(datetimee)


# In[418]:


PlotCount(dfFri)





