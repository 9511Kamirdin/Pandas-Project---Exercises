#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[3]:


df = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas6\Ice Cream Ratings.csv")
df = df.set_index('Date')
df


# In[9]:


df.plot(kind = 'line', title = 'Ice Cream Ratings',xlabel = 'Daily Rating', ylabel = 'Scores')


# In[ ]:





# In[11]:


df.plot(kind = 'bar',stacked = True)


# In[12]:


df['Flavor Rating'].plot(kind = 'bar',stacked = True)


# In[13]:


df.plot.barh(stacked = True)


# In[ ]:





# In[16]:


df.plot.scatter(x = 'Texture Rating',y = 'Overall Rating', s = 300,c = 'Green' )


# In[ ]:





# In[18]:


df.plot.hist(bins = 20)


# In[ ]:





# In[19]:


df.boxplot()


# In[ ]:





# In[21]:


df.plot.area(figsize = (10,5))


# In[ ]:





# In[25]:


df.plot.pie(y='Flavor Rating',figsize = (10,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




