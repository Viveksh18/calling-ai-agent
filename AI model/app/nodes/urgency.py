import json

from app.llm import model
from app.prompts.urgency_prompt import urgency_prompt
from app.state import CallState, Urgency
from langchain_core.messages import SystemMessage


def urgency_node(state: CallState) -> dict:

    response = model.invoke([
        SystemMessage(
            content=urgency_prompt
            + """

Return ONLY valid JSON.

Use exactly this structure:

{
    "level": "LOW",
    "reason": ""
}

The level must be exactly one of:

LOW
NORMAL
MEDIUM
HIGH
CRITICAL
"""
        ),
        *state["conversation"]
    ])

    data = json.loads(response.content)

    urgency = Urgency(**data)

    return {
        "urgency": urgency
    }