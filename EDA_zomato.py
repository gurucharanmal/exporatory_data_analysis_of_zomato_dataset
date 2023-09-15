import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 


df=pd.read_csv('zomato.csv')

df.drop(columns=['url','address','phone','dish_liked','reviews_list','menu_item'],inplace=True)

df.head()

df['rate'].unique()

def set_rate(value):
    if value=='NEW' or value=='-':
        return None
    else:
        value = str(value).split('/')[0]
        return float(value)

df['rate']=df['rate'].apply(set_rate)

df['rate'].unique()

df['rate'].fillna(value=np.mean(df['rate']),inplace=True)

df['rate'].info()

df.info()

df['location'].info()

df['location'].unique()

total_value=df['location'].value_counts(ascending=False)

def set_location(value):
    if value in total_value_less_100:
        return 'others'
    else:
        return value

total_value_less_100=total_value[total_value<100]

df['location']=df['location'].apply(set_location)

total_value=df['location'].value_counts(ascending=False)

total_value

df['location'].info()

df['location'].fillna(value='other',inplace=True)

df['location'].info()

df.head()

df.info()

df['rest_type'].unique()

total=df['rest_type'].value_counts(ascending=False)

total_less_500=total[total<500]


def set_rest_type(value):
    if value in total_less_500:
        return 'others'
    else:
        return value

df['rest_type']=df['rest_type'].apply(set_rest_type)

total=df['rest_type'].value_counts(ascending=False)

total

df.info()

df['rest_type'].unique()

df['rest_type'].fillna(value='other',inplace=True)

df['rest_type'].info()

df.head()

df.info()

df['cuisines'].info()

df['cuisines'].unique()

df.info()

total=df['cuisines'].value_counts(ascending=False)

total_less_25 = total[total<25]

def set_cuisines(value):
    if value in total_less_25:
        return 'other'
    else:
        return value

df['cuisines']=df['cuisines'].apply(set_cuisines)

df['cuisines'].fillna(value='other',inplace=True)

df['cuisines'].info()

df.info()

df['approx_cost(for two people)'].unique()

def set_cost2people(value):
    new=str(value)
    if ',' in new:
        new = new.replace(',' ,'')
        return float(new)
    else:
        return float(value)
        
        

df.rename(columns={'approx_cost(for two people)':'cost2people','listed_in(type)' : 'list_type','listed_in(city)':'list_citys' },inplace=True)

df.head()

df['cost2people']=df['cost2people'].apply(set_cost2people)

df['cost2people'].unique()

df['cost2people'].info()

df['cost2people'].fillna(value=np.mean(df['cost2people']),inplace=True)

df['cost2people'].info()

import sweetviz as sv

df.drop_duplicates(inplace=True)

report=sv.analyze(df)

report.show_html('EDA_analyze.html')

df.head()

plt.hist(df['online_order'])

plt.hist(df['book_table'])

plt.figure(figsize=(16,10))
plt.xticks(rotation=90)
plt.hist(df['location'],150)

plt.figure(figsize=(16,10))
plt.xticks(rotation=90)
plt.hist(df['list_citys'],150)

df.head()

#plt.figure(figsize=(16,10))
plt.xticks(rotation=90)
plt.hist(df['cost2people'],150)

df['votes'].unique()

df['votes']

