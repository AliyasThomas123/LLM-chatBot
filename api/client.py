import streamlit as st
import requests

def get_code(text_input):
    json  = {
       "input" :{"topic": text_input}
    }
    res=requests.post(url = "http://localhost:8000/codes/invoke" , json=json)
    return res.json()['output']

def get_story(text_input):
    json  = {
        "input" :{"topic": text_input}
    }
    res=requests.post(url = "http://localhost:8000/story/invoke" , json=json)
    return res.json()['output']



st.title("Codes and Stosries")
input1 = st.text_input("Write a code on.....?")
input2  = st.text_input("Write a description on ....?")

if input1:
    st.success(get_code(input1))
if input2:
    st.success(get_story(input2))
