## Script to read ACT population projection dataset and calculate the percentage growth from 2015 to 2019 for each ACT suburb based on user suburb input
## Created by Vid dhamodaran
## Initial Draft on 07/06/2019

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Create the dataframe from CSV source
df = pd.read_csv(r"C:\Users\DhamodV\Documents\Data_Sets\ACT_Population_Projections_by_Suburb__2015_-_2020_.csv", encoding="utf-8", skipinitialspace=True)

#Sort the dataframe based on suburb column
df = df.sort_values(by = ['Suburb'], ascending = True)

#Remove any white space in the suburb names
df['Suburb'] = df['Suburb'].str.replace(' ', '')

#Replace Year column values with only year like 2015 from datetime values
df['Year'] = pd.DatetimeIndex(df['Year']).year

#Get Distinct suburb names
suburb_list=df['Suburb'].unique().tolist()

#Get the user preferred suburb name
print("\n\n\n##################  	Choose a Suburb From The List of ACT Suburbs  	##################\n\n")
print(suburb_list)
input_suburb = input("\n\nEnter a Suburb name: ")

#initiate an empty dictionary
dic = {}

#Create a temporary dataframe to select the data from original dataframe based on user entered suburb
selected_df = df.loc[df['Suburb'] == input_suburb]

#Convert the dataframe into a dictionary with keys as column names and values are list of column data
dic = selected_df.to_dict('list')

#Select data to plot
year = dic['Year']
population = dic['Total Population']

#create a Line plot
x = np.array(year)
y = np.array(population)
my_xticks = year
plt.xticks(x, my_xticks)
plt.plot(x, y)
plt.show()












