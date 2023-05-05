import streamlit
import pandas
import requests
import snowflake.connector
import json
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
#def get_country_data(country_choice):
  #country_response = requests.get("https://fruityvice.com/api/fruit/" + this_country_choice) 
  #countries_selected2 = streamlit.multiselect("Pick your destination:", list(my_country_list_all.index),['France','Spain'])
  #countries_to_show2 = my_country_list_all.loc[countries_selected]
# Display the table on the page.
 # return streamlit.dataframe(countries_to_show2)


  

streamlit.header("Travel Destination Advice!")
try:
  country_choice = streamlit.text_input('What country would you like information about?')
  if not country_choice:
    streamlit.error("Please select a country to get information.")
  else:
    
    countries_json=pandas.read_json("./Countries-Europe_complete.json")
    
    #take the json version of the response and normalize it
   

    #country_normalized = pandas.json_normalize(countries_json['sites'][0])
    #data = countries_json
    
    #country_normalized = pandas.json_normalize(data, record_path="./Countries-Europe_complete.json", sep= ';')
    #country_normalized = pandas.json_normalize(data, meta = f"""{./}Countries-Europe_complete.json""", sep= ';')
   
    #country_normalized=pandas.json_normalize(countries_json, max_level=1)
    #country_normalized=data.json(body, expanded=True)

    dic= [
 {
   "name": "Ukraine",
   "country": "UA",
   "continent": "eu",
   "sites": "Bukovel",
   "best_dish": "borscht"
 },
 {
   "name": "France",
   "country": "FR",
   "continent": "eu",
   "sites": [
      "Paris",
      "Monaco",
      "Monte Carlo"
  ],
   "best_dish": "cassoulet"
 },
 {
   "name": "Spain",
   "country": "ES",
   "continent": "eu",
   "sites": "Barcelona",
   "best_dish": "paella"
 },
 {
   "name": "Sweden",
   "country": "SE",
   "continent": "eu",
   "sites": "Stockholm",
   "best_dish": "meatballs"
 },
 {
   "name": "Germany",
   "country": "DE",
   "continent": "eu",
   "sites": "Munchen",
   "best_dish": "sauerbraten"
 },
 {
   "name": "Finland",
   "country": "FIN",
   "continent": "eu",
   "sites": "Helsinki",
   "best_dish": "karelian pastry"
 }
]

    #df=pandas.json_normalize(dic)
    #countries_to_show2 =df.loc[country_choice]    
    # output in the screen as a table
    #streamlit.dataframe(countries_to_show2)
    
    
    def flatten_json(y):
      out = {}

      def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

      flatten(y)
      return out
  
  flat = flatten_json(dic)
  json_normalize(flat)
  

    
    #back_from_function=get_country_data(country_choice)
    #streamlit.dataframe(back_from_function)
    
    # OK my_country_list_all=pandas.read_csv("./Countries-Europe_complete.csv",encoding='utf-8')
    # OK my_country_list_all=my_country_list_all.set_index('name')
    # OKcountries_to_show2 = my_country_list_all.loc[country_choice]
    
    # OK streamlit.dataframe(countries_to_show2)
except URLError as e:
    streamlit.error()
