'''
Feature Engineering helps in Data Cleaning process .
Helps in finding the outliers .
Filling the Nan / Gaps 

It is a process of extracting the useful features from raw data using maths , statistics and domain knowledge .

'''
# Removal using percentile values

# If given with height and name with the person dataset 

import pandas as pd
df = pd.read_csv('person.csv')

max_threshold = df['height'].quantile(0.95)
min_threshold = df['height'].quantile(0.05)

df[df['height']<max_threshold & df['height']>min_threshold] # will show only the desired value of the heights 

# If given a house and rent dataset  

import pandas as pd
df = pd.read_csv('house.csv')

min_threshold , max_threshold = df['rent'].quantile([0.05,0.95])









# Removing using standard deviation

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heights.csv')
plt.hist(df['height'], bins=20, rwidth=0.8)
plt.xlabel('Height')
plt.ylabel('Count')


df.height.std() # gives the std deviation
df.height.mean() # gives the mean

upper_limit = df['height'].mean() + 3*df['height'].std()
lower_limit = df['height'].mean() - 3*df['height'].std()

df[(df['height']>lower_limit) & (df['height']<upper_limit)] # gives the desired values of the heights






# Removing using z_score 
z = (x - mean) / std_dev

df['zscore']= (df.height - df.height.mean()) / df.height.std()

df[(df['zscore']<3) & (df['zscore']>-3)] # gives the desired values of the heights




# removing using IQR Technique 
'''
min
Q1 -> 25th percentile
Q2 -> 50th percentile
Q3 -> 75th percentile
max



Here in the process we calculate the 25th and 50th and 75th percentile calues
and then subtract the values of 75th and 25th percentile values to get the IQR value .

lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
'''
