import streamlit

streamlit.title('My Parents new health diner')
streamlit.header('👌Breakfast Favorites')
streamlit.text('🍵Yogurt and Cherrios')
streamlit.text('🥬Spinach Kale Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
