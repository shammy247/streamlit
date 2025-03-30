import streamlit as st
import pandas as pd
import json

def decode_response(response: str) -> dict:
    response_dict = json.loads(response) #to convert the string to json dictionary
    return response_dict

def write_response(response_dict: dict):
    if "answer" in response_dict:
        st.write(response_dict["answer"])
    