import pandas

movies_dataframe = pandas.read_csv("movies.csv")

movies_dataframe

ratings_dataframe = pandas.read_csv("ratings.csv")

ratings_dataframe
unique_movies = ratings_dataframe["movieId"].unique()
unique_movies
len(unique_movies)

HIGHEST_RATING = 5 
highest_ratings_dataframe = ratings_dataframe.loc[ratings_dataframe["rating"] == HIGHEST_RATING,:]
highest_ratings_dataframe
len(highest_ratings_dataframe)
