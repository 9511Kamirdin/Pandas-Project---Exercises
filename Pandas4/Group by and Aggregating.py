#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas4\Flavors.csv")
df


# In[13]:


group_by_frame = df.groupby('Base Flavor')


# In[14]:


df.groupby('Base Flavor').mean()


# In[15]:


df.groupby('Base Flavor').count()


# In[16]:


df.groupby('Base Flavor').min()


# In[17]:


df.groupby('Base Flavor').max()


# In[18]:


df.groupby('Base Flavor').sum()


# In[23]:


df.groupby('Base Flavor').agg({'Flavor Rating':['max','min','sum'],'Texture Rating':['max','min','sum']})


# In[24]:


df.groupby(['Base Flavor','Liked']).mean()


# In[25]:


df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating':['max','min','sum']})


# In[26]:


df.groupby('Base Flavor').describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




