__author__ = 'Will'

import pandas as pd

users = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\users.csv")
movies = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\movies.csv")
ratings = pd.read_csv("C:\\Users\\Will\\Desktop\\ml-1m\\ratings.csv")
user_ratings = users.merge(ratings, on= 'UserID')
user_ratings = user_ratings.dropna(axis=1)
user_ratings_movies = user_ratings.merge(movies, on= 'MovieID')
user_ratings_movies = user_ratings_movies.dropna(axis=1)

user_ratings_movies.sort_values(by='UserID', ascending=True, inplace=True)


user_ratings_movies.to_csv("C:\\Users\\Will\\Desktop\\ml-1m\\DataSet\\mergedData.csv", index=False)