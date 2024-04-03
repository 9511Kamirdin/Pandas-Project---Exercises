#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas5\LOTR.csv")
df1


# In[4]:


df2 = pd.read_csv(r"D:\Alex - the_analyst - bootcamp\Pandas\Pandas5\LOTR 2.csv")
df2


# In[8]:


df1.merge(df2, how = 'inner', on = ['FellowshipID','FirstName'])


# In[9]:


df1.merge(df2, how = 'outer')


# In[10]:


df1.merge(df2, how = 'left')


# In[11]:


df1.merge(df2, how = 'right')


# In[12]:


df1.merge(df2, how = 'cross')


# In[ ]:





# In[13]:


df1.join(df2, on = 'FellowshipID',how = 'outer',lsuffix = '_Left', rsuffix = '_Right' )


# In[16]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'),lsuffix = '_Left', rsuffix = '_Right', how = 'outer')
df4


# In[ ]:





# In[17]:


pd.concat([df1,df2])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




