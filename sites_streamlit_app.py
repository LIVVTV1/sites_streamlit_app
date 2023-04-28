'''import streamlit
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
my_country_list=pandas.read_csv("https://github.com/LIVVTV1/sites_streamlit_app/blob/main/Countries-Europe.csv", sep=',',header=None,encoding='utf-8')
#https://github.com/ajturner/acetate/blob/master/places/Countries-Europe.csv

my_country_list=my_fruit_list.set_index('name')

countries_selected = streamlit.multiselect("Pick your destination:", list(my_country_list.index),['France','Italy'])
countries_to_show = my_country_list.loc[countries_selected]
'''

import snowflake.connector
import streamlit as st
#from snowflake.snowpark import Session

st.title('❄️ How to connect Streamlit to a Snowflake database')


'''
# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Connected to Snowflake!")
'''


# Load data table
@st.cache_data
def load_data(table_name):
    ## Read in data table
    st.write(f"Here's some example data from `{table_name}`:")
    table = session.table(table_name)
    
    ## Do some computation on it
    table = table.limit(100)
    
    ## Collect the results. This will run the query and download the data
    table = table.collect()
    return table

# Select and display data table
table_name = "DEMO_DB.PUBLIC.COUNTRIES"

## Display data table
with st.expander("See Table"):
    df = load_data(table_name)
    st.dataframe(df)

## Writing out data
for row in df:
    st.write(f"{row[0]} has a :{row[1]}:")
