'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv("data/imdb_1000.csv")

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes


# calculate the average movie duration
movies.columns
movies.duration.mean()
movies.describe()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration').head(1)
movies.sort('duration').tail(1)

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind="hist", bins=30)

# use a box plot to display that same data
movies.boxplot(column="duration", by="genre")
movies.boxplot(column="duration", by="content_rating")


'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.content_rating.value_counts()
### check total
movies.groupby('content_rating').size().sum() # 976 count
movies.content_rating.isnull().sum() # missing 3 counts
movies.describe()  # 979 counts

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind="bar")
plt.title("Number of Movies Per Content Rating")
plt.ylabel('Number of Movies')
plt.xlabel('Content Rating')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace(['NOT RATED','APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace=True)
movies.content_rating.value_counts()

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(['X','TV-MA'], 'NC-17', inplace=True)
movies.content_rating.value_counts()

# count the number of missing values in each column
movies.isnull().sum()

# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
### fill using forward fill
movies.content_rating.fillna(method='ffill', inplace=True)

# calculate the average star rating for movies 2 hours or longer,
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration >= 120].star_rating.mean()
movies[movies.duration < 120].star_rating.mean()

# use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind="scatter", x="star_rating", y="duration", alpha=0.3)
movies.boxplot(column="duration", by="star_rating")
### The majority of movies with 7.4 to 8.7 star rating have a duration range between 100 to 150.
### Movies that are of higher star rating appears to have longer duration

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.content_rating.value_counts()
movies["content_rating_num"] = movies.content_rating.factorize()[0]
movies.plot(kind="scatter", x="content_rating_num", y="duration", alpha=0.3)
movies.hist(column="duration", by="content_rating_num", sharex=True, sharey=True)
### There are a lot more PG rated (0) movies that have longer duration (2 hours or more)

# determine the top rated movie (by star rating) for each genre
high_ratings = movies.groupby('genre').star_rating.max()
for index, value in high_ratings.iteritems():
    print movies[(movies.genre == index) & (movies.star_rating == value)]

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.duplicated("title").sum()
movies[movies.duplicated("title")]

# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
