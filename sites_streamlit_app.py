import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Best sites to visit')
streamlit.header('Travel objectives')
streamlit.text('🪂 Things to do')
streamlit.text('🏞️ Sites to visit')
streamlit.text('🍲 Traditional food')

streamlit.header('🏖️ Choose your holiday destination ⛵')

#import pandas
my_country_list=pandas.read_csv("https://github.com/ajturner/acetate/commit/7c22bfb99989e511726b0aa2cc4b4f7e7308699d")
my_country_list=my_fruit_list.set_index('name')

countries_selected = streamlit.multiselect("Pick some fruits:", list(my_country_list.index),['France','Italy'])
countries_to_show = my_country_list.loc[countries_selected]
