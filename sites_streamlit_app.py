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
# Display the table on the page.
streamlit.dataframe(countries_to_show)



#create function
def get_country_data(country_choice):
  #country_response = requests.get("https://fruityvice.com/api/fruit/" + this_country_choice)
  #contry_normalized = pandas.json_normalize(fruityvice_response.json())
  #return country_normalized
  
  my_country_list_all=pandas.read_csv("./Countries-Europe_complete.csv",encoding='utf-8')
  
  countries_selected2 = streamlit.multiselect("Pick your destination:", list(my_country_list_all.index),['France','Spain'])
  countries_to_show2 = my_country_list_all.loc[countries_selected]
# Display the table on the page.
  return streamlit.dataframe(countries_to_show2)


  

streamlit.header("Travel Destination Advice!")
try:
  country_choice = streamlit.text_input('What country would you like information about?')
  if not country_choice:
    streamlit.error("Please select a country to get information.")
  else:
    #import requests
    #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    #take the json version of the response and normalize it
    #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # output in the screen as a table
    #streamlit.dataframe(fruityvice_normalized)
    
    back_from_function=get_country_data(country_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()
