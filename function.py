import streamlit as st
import pickle 
import pandas as pd 
import numpy as np 
from time import time
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec 

food_dict = pickle.load(open('food_dict.pkl', 'rb'))
df = pd.DataFrame(food_dict)
food_list = df['recipe_name'].values

df_new_dict = pickle.load(open('df_new_dict.pkl', 'rb'))
df_new = pd.DataFrame(df_new_dict)
df_new.set_index('recipe_id', inplace=True)

pt_dict = pickle.load(open('pt_dict.pkl', 'rb'))
pt = pd.DataFrame(pt_dict)

popular_recepies_dict = pickle.load(open('popular_recepies_dict.pkl', 'rb'))
popular_recepies= pd.DataFrame(popular_recepies_dict)


## Content based Recommendation:
def content_recommender(recipe_name):
    recipe_id = df[df['recipe_name']==recipe_name].set_index('recipe_id').index[0]
    start = time()
    
    allRecipes = pd.DataFrame(df_new.index)
    allRecipes = allRecipes[allRecipes.recipe_id != recipe_id]
    allRecipes["distance"] = allRecipes["recipe_id"].apply(lambda x: cosine(df_new.loc[recipe_id][0], df_new.loc[x][0]))
    TopNRecommendation = allRecipes.sort_values(["distance"]).head(3).sort_values(by=['distance', 'recipe_id'])
    # sort by distance then recipe id, the smaller value of recipe id will be picked. 
    
    recipe_df = df.set_index('recipe_id')
    recipe_id = [recipe_id]
    recipe_list = []
    image_list = []
    image_path = '/mnt/C4B416C4B416B93E/Data_Science/Food/raw-data-images/{}.jpg'
    for recipeid in TopNRecommendation.recipe_id:
        recipe_id.append(recipeid)   # list of recipe id of selected recipe and recommended recipe(s)
        recipe_list.append("{}".format(df[df['recipe_id']==recipeid].set_index('recipe_name').index[0]))
        image_list.append(image_path.format(recipeid))
    return zip(recipe_list, image_list)


## Collaborative Filtering Based Recommender System
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

def collaborative_reccommender(food):
    index = np.where(pt.index==food)[0][0]
    distances = similarity_scores[index]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x:x[1], reverse=True)[1:4]

    recipe_name = []
    recipe_id = []
    image_list = []
    image_path = '/mnt/C4B416C4B416B93E/Data_Science/Food/raw-data-images/{}.jpg'
    for i in similar_items:
        recipe_name.append(pt.index[i[0]])
        recipe_id.append(df[df['recipe_name']==pt.index[i[0]]].set_index('recipe_id').index[0])
        image_list.append(image_path.format(df[df['recipe_name']==pt.index[i[0]]].set_index('recipe_id').index[0]))
    return zip(recipe_name, image_list)


## Popularity based recommendations (when we get error in collaborative_recommender):
def popular_reccommender(N):
    popular_N = np.random.choice(popular_recepies['recipe_name'], N)
    recipe_name = []
    recipe_id = []
    image_list = []
    image_path = '/mnt/C4B416C4B416B93E/Data_Science/Food/raw-data-images/{}.jpg'
    for i in popular_N:
        recipe_name.append(i)
        recipe_id.append(df[df['recipe_name']==i].set_index('recipe_id').index[0])
        image_list.append(image_path.format(df[df['recipe_name']==i].set_index('recipe_id').index[0]))

    return zip(recipe_name, image_list)