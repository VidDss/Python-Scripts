## Script to read ACT population projection dataset and calculate the percentage growth from 2015 to 2019 for each ACT suburb based on user suburb input
## Created by Vid dhamodaran
## Initial Draft : 07/06/2019
## Version 1 : 11/06/2019 - added postcode by joining australian postcode dataset 
## Version 2 : 12/06/2019 - added scatter and bar graphs

#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Create the population projection dataframe from CSV source
df = pd.read_csv(r"C:\Users\DhamodV\Documents\Data_Sets\ACT_Population_Projections_by_Suburb__2015_-_2020_.csv", encoding="utf-8", skipinitialspace=True)

#Create the suburb with postcode dataframe from CSV source
df_postcode = pd.read_csv(r"C:\Users\DhamodV\Documents\Data_Sets\australian_postcodes.csv")

#print(df_postcode)

#Sort the dataframe based on suburb column
df = df.sort_values(by = ['Suburb'], ascending = True)

#Remove any white space at both ends of a suburb name
df['Suburb'] = df['Suburb'].str.strip()

#Change the Suburb columns to upper case to match with postcode dataset
df['Suburb'] = df['Suburb'].str.upper()

#Replace Year column values with only year like 2015 from datetime values
df['Year'] = pd.DatetimeIndex(df['Year']).year

#Get Distinct suburb names and locality
suburb_list=df['Suburb'].unique().tolist()
locality_list = df_postcode['locality'].unique().tolist()
#print(len(suburb_list))


#Insert a empty column to accommodate postcode for each suburb
df["Postcode"] = ""

for s in suburb_list:
	if s in (locality_list):
		#Create a temporary dataframe from postcode dataframe based on suburb from population projection dataframe
		df_postcode_match = df_postcode.loc[df_postcode['locality'] == s]
		#get the postcode for ACT
		postcode_match = df_postcode_match.loc[df_postcode_match['State'] == 'ACT', 'postcode'].iloc[0]
		#Copy the extracted postcode for selected suburb into population projection dataframe
		df.loc[df['Suburb'] == 	s, 'Postcode'] = postcode_match
		

	elif s in ('Gungahlin TC','Gungahlin East','Gungahlin West'):
		#Populate Gunghalin TC, East and West suburbs with Gungahlin postcode
		df.loc[df['Suburb'] == 'Gungahlin TC', 'Postcode'] = '2912'
		df.loc[df['Suburb'] == 'Gungahlin East', 'Postcode'] = '2912'
		df.loc[df['Suburb'] == 'Gungahlin West', 'Postcode'] = '2912'
		
	else:
		#Populate the unmatched suburbs with default canberra postcode
		df.loc[df['Suburb'] == s, 'Postcode'] = '2600'
		

#Get Distinct post codes
postcode_list = df['Postcode'].unique().tolist()
print(postcode_list)

df.to_csv(r"C:\Users\DhamodV\Documents\extract.csv", encoding ='utf-8', index= False)
	
#Get the user preferred suburb name
print("\n\n\n##################  	Choose a Suburb From The List of ACT Suburbs  	##################\n\n")
print(suburb_list)
input_suburb = input("\n\nEnter a Suburb name: ").upper()

#initiate an empty dictionary
dic = {}

#Create a temporary dataframe to select the data from original dataframe based on user entered suburb
temp_df = df.loc[df['Suburb'] == input_suburb]


#Convert the dataframe into a dictionary with keys as column names and values are list of column data
dic = temp_df.to_dict('list')
#print(dic)


#Select data to plot
year = dic['Year']
population = dic['Total Population']
postcodes = dic['Postcode']
postcode = postcodes[0]

#Difference in population growth to plot y axis in equal intervals
pop_increase = max(population) - min(population)
yaxis_interval = round((pop_increase/len(year)))
'''
#First Graph - Line plot
x = np.array(year)
y = np.array(population)
my_xticks = year
plt.xticks(x, my_xticks)
plt.yticks(np.arange(min(y),max(y)+1, yaxis_interval))
plt.title("Population Growth from 2015 to 2019 for {0} - {1}".format(input_suburb,postcode))
plt.plot(x, y)
plt.show()


#Second graph - Scatter graph
y_data = np.array(population, dtype=np.float32)
fig, ax = plt.subplots()
ax.scatter(year, y_data)
ax.set_xlabel('Year')
ax.set_ylabel('Population of {0}'.format(input_suburb))
plt.title("Population Growth from 2015 to 2019 for {0} - {1}".format(input_suburb,postcode))
plt.show()
'''
#Third graph - Bar graph

x = np.array(year)
y = np.array(population)
plt.bar(x, y, align='center', alpha=0.5, color='g')
plt.xlabel('Year')
plt.ylabel('Population of {0}'.format(input_suburb))
plt.title("Population Growth from 2015 to 2019 for {0} - {1}".format(input_suburb,postcode))
plt.show()

