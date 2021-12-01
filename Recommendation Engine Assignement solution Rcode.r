# Name: Pradyumna Mohani
# 
# Professional course in Data science and AI
# 
# Batch : 04-11-2020
# 
# Recommendation Engine Assignment Solution
# 

# Q) Build a recommender system with the given data using UBCF.
# Description of the data
# In this dataset have users on the rows rated the jokes in the columns. The dataset comprises
# two csv files, Jokes.csv and Rating.csv is formatted as an excel file. The Jokes file consist of
# joke_id and Jokes & Rating.csv has the ratings given by the users to the jokes. Each rating is
# from (-10.00 to +10.00) and 99
# corresponds to a null rating (user did not rate that joke). Note that the ratings are real
# values ranging from -10.00 to +10.00.

library(recommenderlab)
library(reshape2)
library(readxl)

joke <- read_excel(file.choose())

joke <- joke[,2:4]

ratings_matrix <- as.matrix(acast(joke, user_id~joke_id, fun.aggregate = mean))

R <- as(ratings_matrix, "realRatingMatrix")

rec = Recommender(R, method="UBCF")

uid = "2538"

joke1 <- subset(joke, joke$user_id == uid)

print("you Rated these Jokes:")

joke1

print("recommendations for you:")

prediction <- predict(rec, R[uid], n=3)

as(prediction, "list")