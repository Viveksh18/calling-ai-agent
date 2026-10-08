import json

from app.llm import model
from app.prompts.call_info_prompt import caller_info_prompt
from app.state import CallState, Caller_info
from langchain_core.messages import SystemMessage


def caller_info_node(state: CallState) -> dict:

    response = model.invoke([
        SystemMessage(
            content=caller_info_prompt
            + """

Return ONLY valid JSON.

Use exactly this structure:

{
    "name": "",
    "relationship": "",
    "phone": "",
    "work": ""
}
"""
        ),
        *state["conversation"]
    ])

    data = json.loads(response.content)

    caller_info = Caller_info(**data)

    return {
        "caller_info": caller_info
    }