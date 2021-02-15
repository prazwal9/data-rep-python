''' ASSIGNMENT 1
    1. Collect dataset of weather and COVID-19 (for given parameters of 30 days of October 2020,  different states of India) from following source.
    2. Find all NA inside the dataset and replace it with median for each attributes.
    3. Display 5 point summary of data distribution for all attributes.'''

import pandas as pd
from matplotlib import pyplot as pl

data = pd.read_csv(r"C:\Users\Zwal's pc\Desktop\A1A2\Meghalaya(75008).csv")
print ("\nThe dataset:\n")
print (data)
pd.set_option("display.max_rows", None, "display.max_columns", None)

data = data.fillna(data.median())       #replacing the null values with the median for the respective attribute
print ("\nThe new dataset after replacing NA with median:\n")
print(data)         #printing the new dataset

print("\nChecking for null values again\n")
print(data.isnull().sum())   #verifying if any null values were left out

print("\nThe 5 point summary of the dataset:\n")
print(data.describe())      #displays the 5 point summary of all the attributes of the dataset
    

