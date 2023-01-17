#!/usr/bin/env python
# coding: utf-8

# # Title: Life Expectancy vs GDP
# ### Author: KlasshDev
# ### Date: 2023.01.16
# ### Source: World Health Organization and the World Bank
# 

# In[5]:


# Imports
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm


# # Initial Data Exploring

# In[6]:


# Load data from csv and print head
healthStats = pd.read_csv('all_data.csv')


# Clean column name
healthStats.rename(columns = {'Life expectancy at birth (years)':'Life_Expectancy'}, inplace = True)
print(healthStats.head())


# In[7]:


# Initial Data Explore
healthStats.info()
healthStats.describe()


# In[28]:


# What Unique info
for column in healthStats:
    print(healthStats[column].unique())

#GDP Info
print(healthStats[healthStats.GDP == healthStats.GDP.max()])
print(healthStats[healthStats.GDP == healthStats.GDP.min()])

# Life expectancy
print(healthStats[healthStats['Life_Expectancy'] 
                  == healthStats['Life_Expectancy'].max()])
print(healthStats[healthStats['Life_Expectancy'] 
                  == healthStats['Life_Expectancy'].min()])

print(healthStats.groupby('Country').agg({'Life_Expectancy': ['mean', 'min', 'max']}))

# Linear Regression line GDP weight on life expectancy
model = sm.OLS.from_formula('Life_Expectancy ~ GDP', data=healthStats)
# Fit the model here:
results = model.fit()
# Print the coefficients here:
print(results.params)


# ### Initial Findings:
# - Only 96 entries in data source
# - From years 2000 - 2015
# - Countries: 'Chile' 'China' 'Germany' 'Mexico' 'United States of America' 'Zimbabwe'
# - Min Life expectency: 44 years
# - Max: 81 years
# - Min GDP: 4.4 Billion (Zimbabwe 2008)
# - Max GDP: 1.8 Trillion (USA 2015)
# - Highest age: 81, Germany 2015
# - Lowest age: 44.3, Zimbabwe 2004
# - Zimbabwe is in rough shape, Mean age is only 50 (from 44.3 to only 60.7)
# - In contrast, Germany's mean is 79! (from 78 - 81)
# - Positive linear relationship between GDP and Life expectancy.

# # Visualizations

# In[26]:


# Average life expectancy by country over time
plt.figure(figsize=(20,20))
ax1 = plt.subplot(2,2,1)
sns.lineplot(x='Year', y='Life_Expectancy', hue='Country', data=healthStats)
plt.title('Country life expectency over time')



# Barplot by country
ax2 = plt.subplot(2,2,3)
sns.barplot(x='Country', y='Life_Expectancy', data=healthStats)
plt.title('Life Expectency by Country')



# Plot GDP and life expectancy
ax3 = plt.subplot(2,2,4)
sns.scatterplot(x=healthStats.GDP, y=healthStats.Life_Expectancy, hue=healthStats.Country)
plt.title('Life expectancy by GDP')



# Plot GDP over years by Country
ax4 = plt.subplot(2,2,2)
sns.lineplot(x='Year', y='GDP', hue='Country', data=healthStats)
plt.title('GDP Over time By Country')
plt.show()


# Plot Life Expectancy vs GDP with Linear Regression Line
sns.lmplot(x='Life_Expectancy', y='GDP', data=healthStats, height=6, aspect=2.5)
plt.title('Life expectancy by GDP')
plt.show()


# # Conclusions
# - While Zimbabwe is starting behind on both GDP and Life Expectency, they've made the biggest improvement. 
# - China (And USA) has seen a spike in GDP, not as dramatic of boost in life expectation
# - There is a positive corrolation between GDP and life expectancy.
# 
# 
