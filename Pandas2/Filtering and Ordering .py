#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


df = pd.read_excel(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas2\world_population_excel_workbook.xlsx")


# In[7]:


df


# In[8]:


df[df['Rank']<=10]


# In[10]:


specific_countries = ['Bangladesh','Brazil']

df[df['Country'].isin(specific_countries)]


# In[11]:


df[df['Country'].str.contains('United')]


# In[12]:


df2 = df.set_index('Country')
df2


# In[13]:


df2.filter(items = ['Continent','CCA3'])


# In[14]:


df2.filter(items = ['Zimbabwe'],axis = 0)


# In[16]:


df2.filter(like = 'United',axis = 0)


# In[17]:


df2.loc['United States']


# In[19]:


df2.iloc[3]


# In[25]:


df[df['Rank']<10].sort_values(by = ['Rank','Country'],ascending = [False,True])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




