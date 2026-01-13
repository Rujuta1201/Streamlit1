import streamlit as st

st.title("some basic commands like slider button etc")

age = st.slider("Select your age", 1 , 25)
city = st.selectbox("Select your city", ["New York", "Los Angeles", "Chicago"])

if st.button("Show details"):
    st.write("age:", age)
    st.write("city:", city)