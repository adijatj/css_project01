# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:58:59 2024

@author: adija
"""

"""
Quiz questions based on the IMDB dataset
"""


"""
#1. What is the highest rated movie in the dataset?
"""

#Import needed package
import pandas as pd

#Read in the movie dataset
movies = pd.read_csv("cssproject1\\movie_dataset.csv")

print(max(movies["Rating"]))  #9.0

#Retrieve entire row for movie with highest rating in the dataset. 
movies.loc[movies['Rating'].idxmax()]

# Rank                                                                 55
# Title                                                   The Dark Knight
# Genre                                                Action,Crime,Drama
# Description           When the menace known as the Joker wreaks havo...
# Director                                              Christopher Nolan
# Actors                Christian Bale, Heath Ledger, Aaron Eckhart,Mi...
# Year                                                               2008
# Runtime (Minutes)                                                   152
# Rating                                                              9.0
# Votes                                                           1791916
# Revenue (Millions)                                               533.32
# Metascore                                                          82.0
# Name: 54, dtype: object


"""
#2. What is the average revenue of all movies in the dataset?
"""

#Find column number of Revenue (Millions)
movies.columns.get_loc("Revenue (Millions)") #10

#Drop all the missing values in Revenue Millions as you can't compute average with them and save as a new dataframe
moviesrevenue_noNAs = movies.dropna(subset="Revenue (Millions)")

#Get the average revenue from this filtered subset

ave_revenue = sum(moviesrevenue_noNAs["Revenue (Millions)"])/len(moviesrevenue_noNAs["Revenue (Millions)"])
print(ave_revenue) #82.96



"""
#3. What is the average revenue of movies from 2015 to 2017 in the dataset?
"""

#First, filter the dataset to only show 2015 - 2017 in the year column
condition = (moviesrevenue_noNAs['Year'] == 2015) | (moviesrevenue_noNAs['Year'] == 2016) | (moviesrevenue_noNAs['Year'] == 2017)
revenue_2015to2017 = moviesrevenue_noNAs[condition]

#Get the average revenue from 2015 - 2017
ave_revenue2015_2017 = sum(revenue_2015to2017["Revenue (Millions)"])/len(revenue_2015to2017["Revenue (Millions)"])
print(ave_revenue2015_2017) #63.10


"""
#4. How many movies were released in the year 2016?
"""

#Apply condition to filter out movies from 2016
condition2 = (movies["Year"] == 2016)

#Use condition to filter the movies dataframe and create a new dataframe
movies2016 = movies[condition2]

print(movies2016.describe()) #297

"""
#5. How many movies were directed by Christopher Nolan?
"""

#Count how many times 'Christopher Nolan' appears in the 'Director' Column
#Using value counts, it creates a frequency count of unique entries
cnolan_count = movies['Director'].value_counts()['Christopher Nolan']
print(cnolan_count) #5

print(f"The number of movies directed by Christopher Nolan is: {cnolan_count}")



"""
#6. How many movies in the dataset have a rating of at least 8.0?
"""

#Count number of movies with a rating of 8.0 or higher using the lambda function


len(movies[movies['Rating'].map(lambda x: x >= 8.0)]) #78



"""
#7. What is the median rating of movies directed by Christopher Nolan?
"""

#Apply condition to filter out movies directed by C. Nolan
cnolan_movies = movies[movies['Director'] == "Christopher Nolan"]
print(cnolan_movies.describe())

#Use this to print a summary information which includes the median 
cnolan_movies["Rating"].median() #8.6



"""
#8. Find the year with the highest average rating?
""" 
#Retrieve entire row for movie with highest rating in the dataset.
movies.loc[movies['Rating'].idxmax()] #2008

# Rank                                                                 55
# Title                                                   The Dark Knight
# Genre                                                Action,Crime,Drama
# Description           When the menace known as the Joker wreaks havo...
# Director                                              Christopher Nolan
# Actors                Christian Bale, Heath Ledger, Aaron Eckhart,Mi...
# Year                                                               2008
# Runtime (Minutes)                                                   152
# Rating                                                              9.0
# Votes                                                           1791916
# Revenue (Millions)                                               533.32
# Metascore                                                          82.0
# Name: 54, dtype: object




"""
#9. What is the percentage increase in number of movies made between 2006 and 2016?
"""
#Filter out movies from the year 2006 - 2016
movies2006to2016 = movies[(movies['Year'] >= 2006) & (movies['Year'] <= 2016)]

movies2006to2016.head() #Same as movies variable which contains same duration

#Use movies instead

#Count the number of movies in every year
movie_counts = movies['Year'].value_counts()

#Count the number of movies in 2006 and 2016
movies_2006 = movie_counts.loc[2006] #44
movies_2016 = movie_counts.loc[2016] #297

#Calculate the percentage increase from 2006 - 2016
pct_increase2006_2016 = ((movies_2016 - movies_2006) / movies_2006) * 100
print(pct_increase2006_2016) #575.0


"""
#10. Find the most common actor in all the movies?
"""

#Split the comma-separated values and turn to a series to create separate rows
actor_names = movies['Actors'].str.split(', ').explode()

actor_names.mode() #Mark Wahlberg



#OR

#Import counter from collections
from collections import Counter

#Use Counter to count occurrences of every actor
actor_names_counts = Counter(actor_names)

#Find the most common actor
most_common_actor = actor_names_counts.most_common(1)

print(most_common_actor) 

#Mark Wahlberg - 15 times




"""
#11. How many unique genres are there in the dataset?
#Note, the "Genre" column has multiple genres per movie. You must find a way to identify them individually.
"""

#Split the comma-separated values and turn to a series just as above

genre = movies['Genre'].str.split(',').explode()
genre.nunique() #20


"""
#12. Do a correlation of the numerical features, what insights can you deduce? 
"""

#Correlation between rating and revenue in millions
import matplotlib.pyplot as plt

plt.scatter(movies['Rating'], movies['Revenue (Millions)'])
plt.xlabel('Ratings')
plt.ylabel('Revenue (Millions)')
plt.title('Relationship between IMDB Ratings and Generated Revenue')
plt.show()


"""
In this plot, it appears that movies with high rating generate a higher revenue. 
"""

#Correlation between Runtime and Revenue

plt.scatter(movies['Runtime (Minutes)'], movies['Revenue (Millions)'])
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Revenue (Millions)')
plt.title('Relationship between Movie Runtime and Revenue Generated')
plt.show()


#Correlation between Runtime and metascore
import matplotlib.pyplot as plt

plt.scatter(movies['Runtime (Minutes)'], movies['Metascore'])
plt.xlabel('Metascore')
plt.ylabel('Runtime (Minutes)')
plt.title('Scatterplot of Runtime and Metascore')
plt.show()

"""
The higher the movie duration, the better the metascore
"""


#Correlation between Metascore and Ratings
import matplotlib.pyplot as plt

plt.scatter(movies['Rating'], movies['Metascore'])
plt.xlabel('Rating')
plt.ylabel('Metascore')
plt.title('Scatterplot of Rating and Metascore')
plt.show()

"""
The higher the metascore, the higher the ratings
"""

#Correlation between Metascore and Revenue
import matplotlib.pyplot as plt

plt.scatter(movies['Metascore'], movies['Revenue (Millions)'])
plt.xlabel('Metascore')
plt.ylabel('Revenue (Millions)')
plt.title('Scatterplot of Metascore and Revenue')
plt.show()

"""
No correlation between metascore and revenue
"""

"""


#Top 5 insights:
    
1. Movies with high rating generate a higher revenue.
2. The higher the movie duration, the better the metascore
3. The higher the metascore, the higher the ratings
4. No correlation between metascore and revenue
5. No correlation between runtime and Revenue



#Recommendation
A longer movie duration greater than 1 hour 30 minutes earns higher scores from critics so movies runtime should be extended beyone 90 minutes for higher ratings
Though user ratings are not influenced by runtime, it appears to be influenced by critics scores, so the critiques should not be ignored when directing new movies.
This is likely to generate higher profits in terms of revenues if adhered to.

"""
