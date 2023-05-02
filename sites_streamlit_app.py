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
my_country_list=pandas.read_csv("./Countries-Europe.csv",encoding='utf-8')
#streamlit.dataframe(my_country_list)

#https://github.com/ajturner/acetate/blob/master/places/Countries-Europe.csv

my_country_list=my_country_list.set_index('name')

countries_selected = streamlit.multiselect("Pick your destination:", list(my_country_list.index),['France','Spain'])
countries_to_show = my_country_list.loc[countries_selected]

