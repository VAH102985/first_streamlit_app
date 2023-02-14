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
streamlit.multiselect("Pick some fruits:",list(My_fruit_list.index))
streamlit.dataframe(My_fruit_list)

