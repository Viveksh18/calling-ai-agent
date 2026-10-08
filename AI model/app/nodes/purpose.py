import json

from app.llm import model
from app.prompts.purpose_prompt import purpose_prompt
from app.state import CallState, Purpose
from langchain_core.messages import SystemMessage


def purpose_node(state: CallState) -> dict:

    response = model.invoke([
        SystemMessage(
            content=purpose_prompt
            + """

Return ONLY valid JSON.

Use exactly this structure:

{
    "purpose_category": "",
    "main_purpose": "",
    "caller_request": "",
    "requested_action": "",
    "important_details": ""
}
"""
        ),
        *state["conversation"]
    ])

    data = json.loads(response.content)

    purpose = Purpose(**data)

    return {
        "purpose": purpose
    }