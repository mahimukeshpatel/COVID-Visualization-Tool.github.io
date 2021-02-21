#!/usr/bin/env python
# coding: utf-8

# In[198]:


get_ipython().run_line_magic('autosave', '15')
import pandas as pd
import matplotlib 
import seaborn as sns
import csv
import numpy as np
import matplotlib.pylab as plt  
import folium


# In[226]:


#Turns CDC covid vaccine csv file into a Dataframe
vacc = pd.read_csv('covid19.csv')  
#Isolates State names and number of people who ahve recieve 1+ doses of the vaccine
oneplus = vacc[['State/Territory/Federal Entity','People with 1+ Doses','Number for Herd Immunity']]
#Sets up chart colors
my_colors = ['purple','lightblue']
#plots dataframe data
ax = oneplus.plot(kind = 'bar', color=my_colors)
ax.set_xticklabels(oneplus['State/Territory/Federal Entity'], rotation=90) #x-ticks labels
plt.xlabel('US States')
plt.ylabel('Millions of People')
plt.rcParams["font.family"] = "monospace"
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18, 10)
# sns.barplot(x ='State/Territory/Federal Entity', y='People with 1+ Doses', data=oneplus)


# In[225]:


#Turns CDC covid vaccine csv file into a Dataframe
usdata= pd.read_csv('national-history.csv')  
#Isolates dates and cases per day
cds = usdata[['Date','Cases', 'Deaths','Hospitalized']]
#Sets colors for plot
colorsh = ['cornflowerblue', 'purple', 'indigo']
cds.plot(kind = 'line', color= colorsh) #plots dataframe data
#Axes labels
plt.xlabel('Days since January 13th 2020')
plt.ylabel('Number of People')
plt.rcParams["font.family"] = "monospace"
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
#print(oneplus)


# In[233]:


#Turns csv into Dataframe
upt = pd.read_csv('usstatepostivetest.csv') 
rx =upt.plot(kind = 'bar', color= 'tab:purple')
rx.set_xticklabels(upt['state'], rotation=90) #x-ticks labels
plt.rcParams["font.family"] = "monospace"
plt.xlabel('States')
plt.ylabel('Postive Test Rate')
plt.rcParams["font.family"] = "monospace"
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)


# In[ ]:





# In[ ]:





# In[ ]:




