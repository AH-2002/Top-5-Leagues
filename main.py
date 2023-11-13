#Importing libararies
import pandas as pd
import numpy as np
import matplotlib as plt

#Importing the data set into data frame
df=pd.read_csv('top5_leagues_player.csv')

#Data Exploration

#Taking a first look on the data
print("The head of data :\n",df.head())
print('-'*50)
print("The tail of data: \n",df.tail())
print('-'*50)
#We can see there is alot of missing values


#Printing the name of columns to see if there is any unimportant column
print("name of data's colums :\n",df.columns)
print('-'*50)
#As we see there are two columns for name, so we will get rid of one of them


#Printing the type of the columns
print("The data types of the columns :\n",df.dtypes)
print('-'*50)
#As we see all of types make sensce


#Checking if there is any missing values
print("Now we will display the columns that have missing values :\n",df.isna().sum())
print('-'*50)
#-------------------------------------------------------------------------------------

#Now let's start data cleaning

#At first we have chosen full name column to drop because it is unimportant
df.drop('full_name',inplace=True,axis=1)

#Now we have to handle missing values
#1-Numberical values
df.fillna(df.mean(numeric_only=True),inplace=True)

#2-Other values
#We will use bfill method
df.fillna(method='bfill',inplace=True)

#Now let's check if we still have missing values
print(df.isna().sum())
print('-'*50)

#We still have missing values so we will use ffill method to handle it
df.fillna(method='ffill',inplace=True)
print(df.isna().sum())
print('-'*50)

#Check if there is any duplicates
duplicates=df[df.duplicated()]
print("The duplicates :\n",duplicates)
print('-'*50)

#As we see we don't have any duplicates

#Now we will display some statistics about data
print("Statistics about data :\n")
print('-'*50)
for column in df.columns:
    stat=df[column]
    print(f"The statistics of {column}:\n {stat.describe()}\n")
    print('-' * 50,"\n")

df.to_csv(r'C:\Users\Abd Elrahman\PycharmProjects\Football_Project\Top5_leagues_player - after data cleaning')

