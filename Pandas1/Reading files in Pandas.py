#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\countries of the world.csv")
df


# In[7]:


df = pd.read_table(r"D:\Alex - the_analyst - bootcamp\Pandas\countries of the world.txt")
df


# In[15]:


df = pd.read_json(r"D:\Alex - the_analyst - bootcamp\Pandas\json_sample.json")
df


# In[16]:


df2 = pd.read_excel(r"D:\Alex - the_analyst - bootcamp\Pandas\world_population_excel_workbook.xlsx", sheet_name='Sheet1')
df2


# In[14]:


pd.set_option('display.max.rows',235)
pd.set_option('display.max.columns',40)


# In[17]:


df2.info()


# In[18]:


df2.shape


# In[20]:


df2.head(10)


# In[21]:


df2.tail(10)


# In[22]:


df2['Rank']


# In[23]:


df2.loc[224]


# In[24]:


df2.iloc[224]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




