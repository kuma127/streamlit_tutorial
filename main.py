# main.py
import streamlit as st

key = "text_input"

st.title("Counter Example")
if "count" not in st.session_state:
    st.session_state.count = 0


def increment_counter():
    st.session_state.count += 1


def change_value():
    st.session_state[key] = "Hello world."


st.button("Increment", on_click=increment_counter)

st.write("Count = ", st.session_state.count)

if key not in st.session_state:
    st.session_state[key] = "Hello"

st.text_input("Message", key=key)
st.button("Click", on_click=change_value)
