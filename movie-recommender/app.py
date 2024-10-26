import pandas as pd
import numpy as np

import pickle

import streamlit as st




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movie=[]
    for i in movies_list:

        rec_movie.append(movies.iloc[i[0]].title)
    return rec_movie

movie_dict=pickle.load(open('movie_list.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender system')

option=st.selectbox('how would you like to select',movies['title'].values)

if st.button('Recommend'):
    recommendation=recommend(option)
    for i in recommendation:
        st.write(i)