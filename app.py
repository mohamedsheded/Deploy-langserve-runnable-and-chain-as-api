from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

# loading API keys
load_dotenv()

# set up LLM using groq 
groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model = "Gemma2-9b-It", groq_api_key=groq_api_key)

# Create prompt template
system_message = "Translate the following context into {langauge}"
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system_message),
        ('user', '{text}')
    ]
)

parser = StrOutputParser()

# chain
chain = prompt | model | parser

#app 
app = FastAPI(
    title = "Langchain server",
    version="1.0",
     description="A simple API server using Langchain runnable interfaces"
)

# chain routers
add_routes(
    app,
    chain,
    path = "chain"
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)