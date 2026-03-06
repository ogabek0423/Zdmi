import streamlit as st

st.title("Salom, Dunyo!")

name = st.text_input("Ismingizni kiriting")

if name:
    st.write(f"Xush kelibsiz, {name}!")

