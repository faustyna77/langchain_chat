from openai import OpenAI
from dotenv import load_dotenv
from pprint import pprint
import os
import json 
import streamlit as st

st.set_page_config(page_title="OpenRouter API", page_icon=":guardsman:", layout="wide")
st.title("Mój osobisty Chatbot ")

load_dotenv()



client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY")
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "fastinatechnology.streamlit.app", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "Faustyna Misiura", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="thudm/glm-z1-32b:free",
  messages=[
    {
      "role": "user",
      "content": "Wat is your name?"
    }
  ]
)

def generate_response(prompt):
    

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "fastinatechnology.streamlit.app", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "Faustyna Misiura", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="thudm/glm-z1-32b:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )
    
    return (completion.choices[0].message.content)


prompt=st.text_input("Wprowadż swoje zapytanie tutaj ")
if st.button("Generuj odpowiedź"):
    response = generate_response(prompt)
    st.write(response)


