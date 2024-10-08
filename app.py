import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
print("KEY",os.getenv("LANGCHAIN_API_KEY"))


prompt = ChatPromptTemplate.from_messages(

      [
        ('system','You are Mikku , the helpful chatbot for code development'),
        ('user','Question:{question}')

      ]
)

LLM =Ollama(model = "llama2")
outputparser = StrOutputParser()
chain = prompt | LLM | outputparser
st.title('CodeKata')
input = st.text_input("Enter your queries")
if input:
  response = chain.invoke({'question':input})
  st.write(response)