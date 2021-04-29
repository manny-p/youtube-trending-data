#!/usr/bin/env python
# coding: utf-8

# # Title

# # Lib Import

# In[15]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np
import seaborn as sns


# In[ ]:


import streamlit as st


st.write(
'''
# Hello World
'''
)


# # Data Collection

# In[17]:


youtube_path = '../data/US_youtube_trending_data.csv'

youtube = pd.read_csv(youtube_path)

df = pd.DataFrame(youtube)


# ## todos

# In[18]:


# add api


# In[19]:


# add json russia data


# In[20]:


# add csv brazil data 


# # Data Processing 

# ## todos 

# In[21]:


# add bar graph for view / like counts category counts


# In[22]:


# inspect data
df.head()


# In[23]:


# add missing category str column
df['category'] = ''


# In[ ]:


# loop through category columnn, map int ids to str values, calc totals

cat_list = ['Film & Animation', 'Autos & Vehicles', 'Music', 'Pets & Animals', 
             'Sports', 'Travel & Events', 'Gaming', 'People & Blogs', 'Comedy', 
             'Entertainment', 'News & Politics', 'Howto & Style', 'Education', 
             'Science & Technology', 'Nonprofits & Activism']

for i,cat in enumerate(df.iterrows()):
    if cat[1].categoryId == 2:
        df.loc[i,'category'] = cat_list[0]
    elif cat[1].categoryId == 1:
        df.loc[i,'category'] = cat_list[1]
    elif cat[1].categoryId == 10:
        df.loc[i,'category'] = cat_list[2]
    elif cat[1].categoryId == 15:
        df.loc[i,'category'] = cat_list[3]
    elif cat[1].categoryId == 17:
        df.loc[i,'category'] = cat_list[4]
    elif cat[1].categoryId == 19:
        df.loc[i,'category'] = cat_list[5]
    elif cat[1].categoryId == 20:
        df.loc[i,'category'] = cat_list[6]
    elif cat[1].categoryId == 22:
        df.loc[i,'category'] = cat_list[7]
    elif cat[1].categoryId == 23:
        df.loc[i,'category'] = cat_list[8]
    elif cat[1].categoryId == 24:
        df.loc[i,'category'] = cat_list[9]
    elif cat[1].categoryId == 25:
        df.loc[i,'category'] = cat_list[10]
    elif cat[1].categoryId == 26:
        df.loc[i,'category'] = cat_list[11]
    elif cat[1].categoryId == 27:
        df.loc[i,'category'] = cat_list[12]
        
    elif cat[1].categoryId == 28:
        df.loc[i,'category'] = cat_list[13]
    elif cat[1].categoryId == 29:
        df.loc[i,'category'] = cat_list[14]

df.category.value_counts()


# In[ ]:


#isolate date 

for i, row in enumerate(df.publishedAt):
    df.loc[i, 'publishedAt'] = row[:10]
    
for i, row in enumerate(df.trending_date):
    df.loc[i, 'trending_date'] = row[:10]


# In[ ]:


# p is for published 
# t = trending 

#split in order to analyze y-y, m-m, and d-d changes 

# Split review dates by year, month and day (strings)
time_split = df.publishedAt.str.split('-', n=2, expand=True)
df['p_year'] = time_split[0]
df['p_month'] = time_split[1]
df['p_day'] = time_split[2]

# Convert review dates into a datetime object
dates = df.publishedAt
df.publishedAt = [d.date() for d in pd.to_datetime(dates)]

# Extract month and year from review dates
df['p_month_year'] = pd.to_datetime(df['publishedAt']).dt.to_period('M')

# Split review dates by year, month and day (strings)
time_split = df.trending_date.str.split('-', n=2, expand=True)
df['t_year'] = time_split[0]
df['t_month'] = time_split[1]
df['t_day'] = time_split[2]

# Convert review dates into a datetime object
dates = df.trending_date
df.trending_date = [d.date() for d in pd.to_datetime(dates)]

# Extract month and year from review dates
df['t_month_year'] = pd.to_datetime(df['trending_date']).dt.to_period('M')


# In[ ]:


df.head()


# In[ ]:


# df.tags.value_counts()
# adf.channelId.value_counts


# In[ ]:




