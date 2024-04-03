#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"D:\Alex - the_analyst - bootcamp\Pandas\DataCleaninginPandas\Customer Call List.xlsx")
df


# In[4]:


df = df.drop_duplicates()
df


# In[10]:


df = df.drop(columns = "Not_Useful_Column")


# In[9]:


df


# In[18]:


df["Last_Name"] = df["Last_Name"].str.lstrip('...')
df["Last_Name"] = df["Last_Name"].str.strip('/')
df["Last_Name"] = df["Last_Name"].str.strip('_')
df


# In[39]:


df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]','')
df


# In[ ]:





# In[26]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])
df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"].str.replace('Na--','')
df


# In[32]:


df[["Street Address","State","Zip_Code"]] = df["Address"].str.split(',', n=2, expand=True)
df


# In[34]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')
df


# In[35]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df


# In[41]:


# df.replace('N/a','')
# df.replace('NaN','')
df.fillna('')


# In[42]:


for x in df.index:
    if df.loc[x,"Do_Not_Contact"]=='Y':
        df.drop(x, inplace = True)

df


# In[43]:


for x in df.index:
    if df.loc[x,"Phone_Number"]=='':
        df.drop(x, inplace = True)

df


# In[44]:


df = df.reset_index(drop = True)
df


# In[ ]:





# In[ ]:





# In[ ]:




