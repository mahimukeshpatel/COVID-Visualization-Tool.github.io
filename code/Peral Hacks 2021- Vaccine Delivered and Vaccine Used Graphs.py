#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Creates a horizontal bar graph of vaccines delievers and vaccines used by each state in the US."""

import matplotlib.pyplot as plt
import pandas as pd
#Imported csv file and use pd to read it
state_vaccines = f"/Users/meghansun/Downloads/vacData1.csv"
df = pd.read_csv(state_vaccines)
#Indicates desired columns to retrieve/ export to be used with graph
df2 = df[['State','Vaccines Delivered','Vaccines Used']]
#Plots a horizontal bar graph of Vaccines Delivered and Vaccines Used, mathced with specified color
ax = df.plot.barh(color={"Vaccines Delivered": '#b3cde3', "Vaccines Used": '#810F7C'})
ax.set_yticklabels(df2['State'])
#Flips the State list so it's alphabethical order
ax.invert_yaxis()
#Labels the x and y axis
ax.set_ylabel("State")
ax.set_xlabel("Doses per million")


# In[3]:


"""Creates a horizontal bar graph of vaccines delievers and vaccines used by each state in the US."""

import matplotlib.pyplot as plt
import pandas as pd
#Imported csv file and use pd to read it
state_vaccines = f"/Users/meghansun/Downloads/vacData2.csv"
df = pd.read_csv(state_vaccines)
#Indicates desired columns to retrieve/ export to be used with graph
df2 = df[['State','Vaccine Delivered','Vaccine Used']]
#Plots a horizontal bar graph of Vaccine Delivered and Vaccine Used, mathced with specified color
ax = df.plot.barh(color={"Vaccine Delivered": '#b3cde3', "Vaccine Used": '#810F7C'})
ax.set_yticklabels(df2['State'])
#Flips the State list so it's alphabethical order
ax.invert_yaxis()
#Labels the x and y axis
ax.set_ylabel("State")
ax.set_xlabel("Doses per million")


# In[4]:


"""Creates a horizontal bar graph of vaccines delievers and vaccines used by each state in the US."""

import matplotlib.pyplot as plt
import pandas as pd
#Imported csv file and use pd to read it
state_vaccines = f"/Users/meghansun/Downloads/vacData3.csv"
df = pd.read_csv(state_vaccines)
#Indicates desired columns to retrieve/ export to be used with graph
df2 = df[['State','Vaccine Delivered','Vaccine Used']]
#Plots a horizontal bar graph of Vaccine Delivered and Vaccine Used, mathced with specified color
ax = df.plot.barh(color={"Vaccine Delivered": '#b3cde3', "Vaccine Used": '#810F7C'})
ax.set_yticklabels(df2['State'])
#Flips the State list so it's alphabethical order
ax.invert_yaxis()
#Labels the x and y axis
ax.set_ylabel("State")
ax.set_xlabel("Doses per million")


# In[5]:


"""Creates a horizontal bar graph of vaccines delievers and vaccines used by each state in the US."""

import matplotlib.pyplot as plt
import pandas as pd
#Imported csv file and use pd to read it
state_vaccines = f"/Users/meghansun/Downloads/vacData4pt2.csv"
df = pd.read_csv(state_vaccines)
#Indicates desired columns to retrieve/ export to be used with graph
df2 = df[['State','Vaccine Delivered','Vaccine Used']]
#Plots a horizontal bar graph of Vaccine Delivered and Vaccine Used, mathced with specified color
ax = df.plot.barh(color={"Vaccine Delivered": '#b3cde3', "Vaccine Used": '#810F7C'})
ax.set_yticklabels(df2['State'])
#Flips the State list so it's alphabethical order
ax.invert_yaxis()
#Labels the x and y axis
ax.set_ylabel("State")
ax.set_xlabel("Doses per million")


# In[6]:


"""Creates a horizontal bar graph of vaccines delievers and vaccines used by each state in the US."""

import matplotlib.pyplot as plt
import pandas as pd
#Imported csv file and use pd to read it
state_vaccines = f"/Users/meghansun/Downloads/vacData5.csv"
df = pd.read_csv(state_vaccines)
#Indicates desired columns to retrieve/ export to be used with graph
df2 = df[['State','Vaccine Delivered','Vaccine Used']]
#Plots a horizontal bar graph of Vaccine Delivered and Vaccine Used, mathced with specified color
ax = df.plot.barh(color={"Vaccine Delivered": '#b3cde3', "Vaccine Used": '#810F7C'})
ax.set_yticklabels(df2['State'])
#Flips the State list so it's alphabethical order
ax.invert_yaxis()
#Labels the x and y axis
ax.set_ylabel("State")
ax.set_xlabel("Doses per million")

