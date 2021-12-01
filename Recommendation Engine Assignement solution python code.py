# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:09:52 2020

@author: Pradyumna Mohani

Professional course in data science and AI

Batch: 04-11-2020

Recommendation Engine Assignment solution

"""
"""
Q) Build a recommender system with the given data using UBCF.
Description of the data
In this dataset have users on the rows rated the jokes in the columns. The dataset comprises
two csv files, Jokes.csv and Rating.csv is formatted as an excel file. The Jokes file consist of
joke_id and Jokes & Rating.csv has the ratings given by the users to the jokes. Each rating is
from (-10.00 to +10.00) and 99
corresponds to a null rating (user did not rate that joke). Note that the ratings are real
values ranging from -10.00 to +10.00.

"""
import pandas as pd
import numpy as np
# import dataset
joke = pd.read_excel("D:/360 DigitMg Data science Assignments/Problem Statement_Assignments/Recommendation Engine/Ratings.xlsx")

joke_ratings = joke.drop("id", axis = 1)

joke_pivot = joke_ratings.pivot_table(values = "Rating", index = "user_id", columns= "joke_id",)

joke_pivot = joke_pivot.fillna(joke_pivot.mean(axis=0))

from sklearn.metrics.pairwise import cosine_similarity

corr_matrix = cosine_similarity(joke_pivot)

user_id1 = joke_ratings.drop_duplicates(subset =["user_id"])

user_index = pd.Series(data = user_id1.index, index = user_id1["user_id"])

def give_recommendation(uid,topN):
    user_identity = user_index[uid]
    cosin_scores = list(enumerate(corr_matrix[user_identity]))
    cosin_scores = sorted(cosin_scores, key=lambda x:x[1], reverse = True)
    cosine_scores_N = cosin_scores[0: topN+1]
    joke_idx  =  [i[0] for i in cosine_scores_N]
    joke_scores = [i[1] for i in cosine_scores_N]
    joke_similar_show = pd.DataFrame(columns=["joke", "Score"])
    joke_similar_show["joke"] = joke_ratings.loc[joke_idx, "joke_id"]
    joke_similar_show["Score"] = joke_scores
    joke_similar_show.reset_index(inplace = True)  
    # anime_similar_show.drop(["index"], axis=1, inplace=True)
    print (joke_similar_show)
    
give_recommendation(9797, 5)
