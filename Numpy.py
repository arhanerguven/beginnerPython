#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CS115 Lab 09 Questions


# ## *Question 01*

# Import numpy

# In[1]:


import numpy as np


# a.	Load the data from the file covid_data.txt into a numpy array, covid_data. 
# b.	Load the data from the file covid_country.txt into a numpy array, covid_country. 

# In[2]:


covid_data = np.loadtxt("covid_data.txt")
covid_country = np.loadtxt("covid_country.txt",skiprows = 1, dtype = "str")


# c.	Transpose and update the covid_data array.

# In[6]:


covid_data = covid_data.T


# d.	Calculate and display the maximum tests per 1 million.

# In[8]:


covid_data.max(axis=1)[2]


# In[21]:


#e.	Display the names of the countries in Asia


# In[9]:


covid_country2 = covid_country.T
ar1 = covid_country2[0][covid_country2[1]=="Asia"]
print(ar1)


# f.	Display the names of the countries with death numbers less than 50

# In[10]:


print("Countries with less than 50 deaths per 1 million:")
ar2 = covid_country2[0][covid_data[1]<50]
print(ar2)


# g.	Calculate and display the average cases per 1 million for Europe.

# In[11]:


print("Average cases per 1 million i Europe:")
ave = covid_data[0][covid_country2[1]=="Europe"]
ave.mean()


# h.	Display the name of the countr(ies) with the minimum total cases per million in Europe(note: there may be more than one country with the same minimum total cases per million in Europe.

# In[12]:


print("Country with minimum total cases per 1 million in Europe:")
case = ave.min()

idx = np.where(covid_data[0] == case)
print(covid_country2[0][idx][0])


# i.	Create a new array, test_result, where the first column contains country names, and the second column contains the deaths per 1 million. Hint: your new array should have 2 columns and 172 rows, not 172 columns and 2 rows.

# In[13]:


test_result = np.array([covid_country2[0],covid_data[1]])
test_result = test_result.T


# j.	Output the data in test_result to a file, test_result.txt.

# In[14]:


np.savetxt("test_result.txt",test_result,fmt = "%s")


# In[ ]:




