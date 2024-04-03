#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas3\world_population.csv")


# In[4]:


df


# In[5]:


df = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas3\world_population.csv", index_col = "Country")
df


# In[6]:


df.reset_index(inplace = True)


# In[7]:


df


# In[9]:


df.set_index('Country',inplace = True)
df


# In[10]:


df.loc['Albania']


# In[11]:


df.iloc[1]


# In[12]:


df.reset_index(inplace=True)


# In[13]:


df.set_index(['Continent','Country'],inplace = True)


# In[16]:


df.sort_index()
pd.set_option('display.max.rows',235)


# In[ ]:





# In[ ]:




