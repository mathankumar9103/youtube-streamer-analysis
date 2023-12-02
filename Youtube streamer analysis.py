#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import os
for dirname, _, filename in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[3]:


url = 'youtubers_df.csv'
df = pd.read_csv(url)


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.describe(include = 'all')


# In[7]:


df.info()


# In[8]:


df.columns


# In[9]:


df["Categories"].info()


# In[10]:


df["Country"].info()


# In[11]:


df["Country"].mode()


# In[13]:


country_youtubers_count = df["Country"].value_counts().head(10)
country_youtubers_count


# In[14]:


import matplotlib.pyplot as plt
country_youtubers_count.plot(kind = "bar")
plt.xlabel("Country")
plt.ylabel("Number of youtubers")
plt.title("Top 10 Countries having Content Creators")
plt.show()


# In[18]:


total_categories = df["Categories"].value_counts()
total_categories.head(15)


# In[19]:


df.dropna(subset = 'Categories',inplace = True)
df.describe()


# In[20]:


df.info()


# In[22]:


categories = df['Categories'].unique()
print("Categories in the dataset:")
for categorie in categories:
    print(categorie)


# In[23]:


total_categories = df["Categories"].value_counts()
total_categories.head(15)


# In[24]:


categories = df["Categories"].value_counts().head(12)
categories.plot(kind = "bar")
plt.xlabel("category")
plt.ylabel("count")
plt.title("Top 12 categories")
plt.show()


# In[28]:


suscribers = df.head(8)
plt.figure(figsize =(10,6))
plt.bar(suscribers['Username'],suscribers['Suscribers'])
plt.xlabel = 'subcribers'
plt.ylabel = 'Youtuber'
plt.title = 'Top 8 Youtube Suscribers'
plt.show()


# In[ ]:




