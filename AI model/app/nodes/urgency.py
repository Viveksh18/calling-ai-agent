from app.llm import model
from app.state import CallState, Urgency, UrgencyLevel
from app.prompts import urgency_prompt
from langchain.messages import SystemMessage

def urgency_node(state: CallState) -> dict:

    structured_output = model.with_structured_output(Urgency)

    response = structured_output.invoke([
        SystemMessage(content=urgency_prompt),
        *state["conversation"]
    ])

    return {
        "urgency": response
    }


