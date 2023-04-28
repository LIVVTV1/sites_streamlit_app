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
my_country_list=pandas.read_csv("https://github.com/LIVVTV1/sites_streamlit_app/blob/main/Countries-Europe.csv", sep=',')
#https://github.com/ajturner/acetate/blob/master/places/Countries-Europe.csv

my_country_list=my_fruit_list.set_index('name')

countries_selected = streamlit.multiselect("Pick your destination:", list(my_country_list.index),['France','Italy'])
countries_to_show = my_country_list.loc[countries_selected]
