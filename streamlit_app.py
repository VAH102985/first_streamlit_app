import streamlit
Import pandas

My_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.Amazon aws.com/dabw/fruit_macros.txt")

streamlit.title("My parents New Healthy Diner")

streamlit.header("Breakfast")


streamlit.text("🫕 Omega 3 & blueberry oatmeal")
streamlit.text("🥗 Kale, Spinach & Rock smoothie")
streamlit.text("🐔 Hard-boiled free-range eggs")
streamlit.text("🥑🍞 Avacado tost")


Streamlit.header("🍌🍓Build your own fruit smoothie🥝🍇")
Streamlit.dataframe(My_fruit_list)
