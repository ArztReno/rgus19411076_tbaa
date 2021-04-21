# date : 22/12/2020
# Author : Renato Gusani
# Student no. : x19411076
# Question 3 – APIs & Data Processing : a1, b1

# * * * * * * * * * * question a.1) * * * * * * * * * *
'''
The following line 10 basically imports the pandas and numpy library, yet rather than utilizing the name pandas, 
it's told to utilize the name as [pd]. This is to make sure I can do [pd] as opposed to composing with [pandas]. The same with numpy'''
import pandas as pd
import numpy as np

# reads the data from the provided CSV file. (Also creating the data frame)
movies = pd.read_csv('movies.csv') 

# a) Get the details of the third movie of the dataset
# Single selection using iloc and DataFrame
# Get the details of the third movie of the DataFrame
third_movie = movies.iloc[3]
print("Details of the third movie:")
print(third_movie) 


# b) Sort the dataset based on the profitability and limiting to top 10 entries
movies.nlargest(10)


# c) Access those movies, released between 2005 and 2010 
movies['Year'] = pd.to_datetime(movies['Year']) # ensuring the 'Year' column is in date format

# setting the desired start date and end date to filter the dataframe with
start_date = '2005'
end_date = '2010'

# setting the mask, I can then apply this to the dataframe to filter it
mask = (movies['Year'] > start_date) & (movies['Year'] <= end_date)

# assigning the mask to the dataframe to return the rows with Year between the specified start/end dates
movies = movies.loc[mask]
movies


# d) Get the movie with the max gross and the movie with the min gross
small_movies = movies[['title', 'Profitability']]
Profitability = small_movies['Profitability']
print(small_movies)
print("**************************************")
print("Top Profitability")
print(Profitability.max())
print("lowest Profitability")
print(Profitability.min())


# e) Use user’s input to dynamically find and display the movies (film, genre, year) with a matching studio
cols = input("Enter a column?")
movies = movies[cols]


# * * * * * * * * * * question b.1) * * * * * * * * * *


# importing required modules 
import requests, json 
  
# Entering my API key (By Registering for the website)
api_key = "4780224cb843e09bb79229b57b9d17db"
  
# foundation_url variable to store url 
foundation_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
city_name = input("Input a city to check weather : ") 
  
# finished_url variable to store 
# finished_url address 
finished_url = foundation_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return reply object 
reply = requests.get(finished_url) 
  
# json method of reply object  
# convert json format data into 
# python format data 
a = reply.json() 
  
''' Now a contains list of nested dictionaries 
    Check the value of "cod" key is equal to 
    404 error", means city is found otherwise, 
    city is not found '''
if a["cod"] != "404 error": 
  
    # store the value of "main" 
    # key in variable b
    b = a["main"] 
  
    # store the value corresponding 
    # to the "temp" key of b 
    current_temperature = b["temp"] 
  
    # store the value corresponding 
    # to the "pressure" key of b 
    wind_speed = b["pressure"] 
  
    # store the value corresponding 
    # to the "humidity" key of b
    current_humidiy = b["humidity"] 
  
    # store the value of "weather" 
    # key in variable c 
    c = a["weather"] 
  
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of c
    weather_description = c[0]["description"] 
  
    # print following values 
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n wind speed (in SI unit) = " +
                    str(wind_speed) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description/weather = " +
                    str(weather_description)) 

# If the above cannot be executed, the following error is given.  
else: 
    print(" Cannot Find Weather Information For The Entered City ") 