
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favourites')


streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')  
streamlit.text('🥑🍞 Avocado Toast')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")

#streamlit.text(fruityvice_response.json())

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruity_choice:
    streamlit.error("Please select gruit");
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError e
  streamlit.error()

streamlit.write('The user entered ', fruit_choice)

# write your own comment -what does the next line do? 

# write your own comment - what does this do?


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("select * from fruit_load_list")
streamlit.dataframe(my_data_row)

fruit_choice = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('The user entered ', fruit_choice)

#my_cur.execute("insert into fruit_load_list values('--')")
