#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset - [No_Show_appointments Data set]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
#  
# 
# This is a data analysis for 100k medical appointments in Brazil and is focused on the question of whether or not patients show up for their appointment.
# 
# ### Notes:
# 
# -‘ScheduledDay’ tells us on what day the patient set up their appointment.
# 
# -‘Neighborhood’ indicates the location of the hospital.
# 
# -‘Scholarship’ indicates whether or not the patient is enrolled in Brasilian welfare program Bolsa Família.
# 
# -Be careful about the encoding of the last column: it says ‘No’ if the patient showed up to their appointment, and ‘Yes’ if they did not show up.
# 
# ### Question(s) for Analysis
# 
# Which factors are important for us to know in order to predict if a patient will show up for their scheduled appointment?
# 
# 
# 

# In[22]:


# packeges I used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





get_ipython().run_line_magic('matplotlip', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# 

# First I loaded the data in a data frame
# 
# Second I started to make an overview using some codes to understand the data
# 
# Then started to clean the data

# In[ ]:


# Loading data 
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.head()


# In[19]:


df.shape #data overview


# In[13]:


df.info() #data overview


# In[20]:


df.describe() #data overview


# In[45]:


df.duplicated().any() #data overview


# In[46]:


df.isnull().sum() #data overview


# 
# ### Data Cleaning
# 
# 
# 
#  

# deleting unnecessary data

# In[18]:



df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'],axis = 1 , inplace = True)
df.head()


# In[8]:


#correcting spelling

df.rename(columns={'No-show' : 'No_show'} , inplace = True)
df.rename(columns={'Hipertension' : 'Hypertension'} , inplace = True)
df.rename(columns={'Handcap' : 'Handicap'} , inplace = True)
df.head()


# ## Exploratory Data Analysis.
# 
# 
# ### visual histograms and conclusions for data 

# visual overview

# In[12]:




df.hist(figsize= (20,20));


# 
# 1/most of patients are not alcoholism')
#       
# 2/it is only about 10% of patients who have diabetes')
#       
# 3/most of patients are not handicapped and don\'t suffer from hypertention')
# 
# 4/ about 66% of patiens didn\'t receive sms')
#       
# 5/ about 10% of patients have a scholaeship')

# In[10]:


show = df.No_show == 'No'  
noshow = df.No_show == 'Yes'

df[show].count() 


# In[29]:


df[noshow].count()


# about 80% of patients attented in thier appointments

# ### Relationships between showing and other variables

# In[26]:



print(df.Gender[show].value_counts())
print(df.Gender[noshow].value_counts())


# In[54]:


plt.figure(figsize = [10,10])
df.Gender[show].hist (label = show)
df.Gender[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a Gender')
plt.xlabel('Gender')
plt.ylabel('patients number');


# In[13]:


print(df.Diabetes[show].value_counts())
print(df.Diabetes[noshow].value_counts())

plt.figure(figsize = [10,10])
df.Diabetes[show].hist (label = show)
df.Diabetes[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a Diabetes')
plt.xlabel('Diabetes')
plt.ylabel('patients number');


# conclusion: Diabetes is insignificant

# In[14]:


print(df.Scholarship[show].value_counts())
print(df.Scholarship[noshow].value_counts())

plt.figure(figsize = [10,10])
df.Scholarship[show].hist (label = show)
df.Scholarship[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a scholarship')
plt.xlabel('scholarship')
plt.ylabel('patients number');


# conclusion : schoralship is insignificant

# In[15]:


print(df.Handicap[show].value_counts())
print(df.Handicap[noshow].value_counts())

plt.figure(figsize = [10,10])
df.Handicap[show].hist (label = show)
df.Handicap[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a Handicap')
plt.xlabel('Handicap')
plt.ylabel('patients number');


# conclusion: Handicap is insignificant

# In[16]:


print(df.Hypertension[show].value_counts())
print(df.Hypertension[noshow].value_counts())

plt.figure(figsize = [10,10])
df.Hypertension[show].hist (label = show)
df.Hypertension[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a Hypertension')
plt.xlabel('Hypertension')
plt.ylabel('patients number');


# conclusion: Hypertension is insignificant

# In[17]:


print(df.Alcoholism[show].value_counts())
print(df.Alcoholism[noshow].value_counts())

plt.figure(figsize = [10,10])
df.Alcoholism[show].hist (label = show)
df.Alcoholism[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and having a Alcoholism')
plt.xlabel('Alcoholism')
plt.ylabel('patients number');


# conclusion: Alcoholism is insignificant 

# In[18]:


print(df.SMS_received[show].value_counts())
print(df.SMS_received[noshow].value_counts())

plt.figure(figsize = [10,10])
df.SMS_received[show].hist (label = show)
df.SMS_received[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and  SMS_received')
plt.xlabel('SMS_received')
plt.ylabel('patients number');


# conclusion: who received a sms and show are less than who did\'t received any sms and show

# First we need to sort age data

# In[55]:


np.sort(df.Age.unique())


# In[57]:


df = df[df.Age >= 0]

np.sort(df.Age.unique())


# In[19]:




plt.figure(figsize = [10,10])
df.Age[show].hist (label = show)
df.Age[noshow].hist (label = noshow)
plt.legend()
plt.title('the relationship between showing and  Age')
plt.xlabel('Age')
plt.ylabel('patients number');


# patients from 0 to 10 are more showed , followed by  from 35 to 55

# In[20]:


plt.figure(figsize = [10,10])
df.Neighbourhood[show].value_counts().plot (kind ='bar' , color= 'red' , label = 'show')
df.Neighbourhood[noshow].value_counts().plot (kind ='bar' , color= 'blue' , label = 'noshow')
plt.legend()
plt.title('the relationship between showing and  Neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('patients number');


# Neighbourhood is significant

# <a id='conclusions'></a>
# ## Conclusions
# 
# 
# 
# 
# 
# 1/It may be strange that most of who didn't receive sms are showed
# 
# 2/there is a relationship between age, neighbourhood and show
# 
# 
# 
# 
# ### Limitations
# 
# 
# There is no strong relationship between showing and other characteristics like Scholarship, Hypertension,Diabetes,	Alcoholism and Handicap
# 

# In[21]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




