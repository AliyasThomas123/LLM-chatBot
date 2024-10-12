from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from langserve import add_routes
from dotenv import load_dotenv
import os
import uvicorn
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
print("KEY",os.getenv("LANGCHAIN_API_KEY"))
app = FastAPI(title="Production Grade Language Models",
description="LLM using API",
version="1.0")

prompt1  = ChatPromptTemplate.from_template("Write a code on {topic}")
prompt2 = ChatPromptTemplate.from_template("Write a description about {topic}")
llm = Ollama(model = "llama2")

add_routes(
    app,
    prompt1|llm,
    path="/codes"
)

add_routes(
    app,
    prompt2|llm,
    path="/story"
)

if __name__ == "__main__":
    uvicorn.run(app=app , port=8000 , host = "localhost")