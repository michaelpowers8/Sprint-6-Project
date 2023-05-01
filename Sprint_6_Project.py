#!/usr/bin/env python
# coding: utf-8

# # Sprint 6 Project

# ## Initializing Data

# In[39]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[40]:


first_query = "project_sql_result_01.csv"
second_query = "project_sql_result_04.csv"


# In[41]:


df_trips_num = pd.read_csv(first_query)
df_trips_average = pd.read_csv(second_query)


# ## Exploratory Data Analysis

# In[42]:


display(df_trips_num.head())
display(df_trips_average.head())


# In[43]:


display(df_trips_num.isna().sum())
display(df_trips_average.isna().sum())


# In[44]:


display(df_trips_average.nlargest(10, columns=["average_trips"]))


# In[89]:


df_trips_num.nlargest(10, columns=['trips_amount']).set_index('company_name').plot(
    kind='pie', 
    y='trips_amount',
    autopct='%1.0f%%', 
    figsize=(10,5), 
    legend=False).set(label=df_trips_num.index)
plt.title('Taxis to Number of Rides')
plt.ylabel("")
plt.show() 


# In[46]:


df_trips_num.nlargest(10, columns=['trips_amount']).set_index('company_name').plot(
    kind='bar', 
    y='trips_amount',
    legend=False).set(label=df_trips_cost.index)
plt.title('Taxis to Number of Rides')
plt.ylabel("Number Rides")
plt.show() 


# In[47]:


df_trips_average.nlargest(10, columns=['average_trips']).set_index('dropoff_location_name').plot(
    kind='pie', 
    y='average_trips',
    autopct='%1.0f%%', 
    figsize=(10,5), 
    legend=False).set(label=df_trips_average.index)
plt.title('Top 10 Dropoff Locations')
plt.ylabel("")
plt.show()


# In[48]:


df_trips_average.nlargest(10, columns=['average_trips']).set_index('dropoff_location_name').plot(
    kind='bar', 
    y='average_trips',
    legend=False).set(label=df_trips_average.index)
plt.title('Top 10 Dropoff Locations')
plt.ylabel("")
plt.show()


# ## Hypothesis Testing

# Null Hypothesis: "The average duration of rides from the Loop to O'Hare International Airport does not change on rainy Saturdays."

# Alternate Hypothesis: "The average duration of rides from the Loop to O'Hare International Airport does changes on rainy Saturdays."

# In[59]:


df_rides = pd.read_csv("/datasets/project_sql_result_07.csv")


# In[60]:


df_rides.head()


# In[69]:


df_rides.describe()


# In[72]:


display(df_rides.isna().sum())


# In[73]:


df_rides['duration_seconds'].plot(kind='box',
                                 title='Time in Loop',
                                 vert=False)


# In[80]:


df_rides['duration_seconds'].plot(kind='hist',
                                 title='Time in Loop',
                                 bins=20)


# In[83]:


df_rides["start_ts"] = pd.to_datetime(df_rides["start_ts"])


# In[84]:


saturday_bad = df_rides[(df_rides["start_ts"].dt.weekday==5)&(df_rides["weather_conditions"]!="Good")]["duration_seconds"].values
saturday_good = df_rides[(df_rides["start_ts"].dt.weekday==5)&(df_rides["weather_conditions"]=="Good")]["duration_seconds"].values


# In[88]:


alpha = 0.05
result = stats.ttest_ind(saturday_bad, saturday_good)
print('pvalue:', result.pvalue)

if (result.pvalue < alpha):
    print("The average duration of rides from the Loop to O'Hare International Airport changes on rainy Saturdays.")
else:
    print("The average duration of rides from the Loop to O'Hare International Airport does not change on rainy Saturdays.")
print(f"Good weather, mean={saturday_good.mean()}")
print(f"Bad weather, mean={saturday_bad.mean()}")


# In[ ]:




