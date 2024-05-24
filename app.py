import streamlit as st
import pickle 
import pandas as pd 
import numpy as np 
from function import content_recommender
from function import collaborative_reccommender
from function import popular_reccommender

food_dict = pickle.load(open('food_dict.pkl', 'rb'))
df = pd.DataFrame(food_dict)
food_list = df['recipe_name'].values
df_new_dict = pickle.load(open('df_new_dict.pkl', 'rb'))
df_new = pd.DataFrame(df_new_dict)


st.title('Food Recommender System :')
selected_food_name = st.selectbox(
    "How would you like to be contacted?",
    food_list)

st.write("You selected:", selected_food_name)

if st.button('Recommend'):
    output1 = content_recommender(selected_food_name)
    try:
        output2 = collaborative_reccommender(selected_food_name)
    except:
        output2 = popular_reccommender(3)

    col1, col2 = st.columns(2, gap='large')
    with col1:
        for i in output1:
            st.markdown("**{}**".format(i[0]))
            st.image(i[1])
    with col2:
        for i in output2:
            st.markdown("**{}**".format(i[0]))
            st.image(i[1])