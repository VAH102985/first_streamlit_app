import streamlit
import pandas

My_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
My_fruit_list = My_fruit_list.set_index("Fruit")


streamlit.title("My parents New Healthy Diner")

streamlit.header("Breakfast")


streamlit.text("🫕 Omega 3 & blueberry oatmeal")
streamlit.text("🥗 Kale, Spinach & Rock smoothie")
streamlit.text("🐔 Hard-boiled free-range eggs")
streamlit.text("🥑🍞 Avacado tost")


streamlit.header("🍌🍓Build your own fruit smoothie🥝🍇")
fruits_selected = streamlit.multiselect("Pick some fruits:",list(My_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = My_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#streamlit.dataframe(My_fruit_list)
streamlit.header('Fruityvice Fruit Advice!')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
