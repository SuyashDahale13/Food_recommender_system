# Hybrid Food_Recommender_System
![Screenshot from 2024-05-25 13-11-29](https://github.com/SuyashDahale13/Food_Recommender_System/assets/138577127/8de7ef6f-2c11-4197-b3f4-980bbc1ab3dd)

## Used Dataset - https://www.kaggle.com/datasets/elisaxxygao/foodrecsysv1

## Recommender System -
A recommender system is a technology that suggests things you might like, like products, movies, or even news articles. 

## Hybrid Recommender System -
A hybrid recommender system is a type of recommendation system that combines multiple recommendation techniques to improve the accuracy and effectiveness of the recommendations provided to users. These systems leverage the strengths of different algorithms while mitigating their individual weaknesses, thus offering a more robust and reliable solution for personalized recommendations.

### Key Components of this Hybrid Food -Recommender Systems

#### Content-Based Filtering (CBF):

- Uses item features and user profiles to recommend items similar to those the user has shown interest in.
- In this project I have used ingredients and nutirions as base for content-based filtering. Used Word2vec technique to convert ingredients into vector form.
![Screenshot from 2024-05-25 13-31-09](https://github.com/SuyashDahale13/Food_Recommender_System/assets/138577127/7a52b266-4a86-40b4-8cb6-dfc6d7c72822)

#### Collaborative Filtering (CF):
- Utilizes user-item interactions to find patterns in user behavior.
There are two main types of collaborative filtering:
1. User-User Collaborative Filtering: Finds users with similar preferences and recommends items they have liked.
2. Item-Item Collaborative Filtering: Recommends items that are similar to items the user has liked in the past.
- I opted for User-User Collaborative Filtering
