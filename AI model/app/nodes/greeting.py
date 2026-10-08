import operator
import os
from app.llm import model # large language model
from app.state import CallState
from app.prompts.greeting_prompt import greeting_prompt
# from typing import TypedDict, List, Optional, Literal, Annotated
# from pydantic import BaseModel, Field
# from langgraph.graph import StateGraph, START, END
# from langgraph.types import Send
# from langchain_core.messages import SystemMessage, HumanMessage



def greeting_node(state: CallState) -> dict:

    response = model.invoke(greeting_prompt)

    greeting = response.content

    return{
        "greeting": greeting 
    }
