import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


# -------Load environment-------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#---------LLM--------------
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY,

)