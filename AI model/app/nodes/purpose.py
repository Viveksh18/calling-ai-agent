from app.llm import model
from app.prompts.purpose_prompt import purpose_prompt
from app.state import CallState, Purpose
from langchain_core.messages import SystemMessage


def purpose_node(state: CallState) -> dict:

    structured_output = model.with_structured_output(Purpose)

    response = structured_output.invoke([
        SystemMessage(content=purpose_prompt),
        *state["conversation"]
    ])

    return {
        "purpose": response
    }