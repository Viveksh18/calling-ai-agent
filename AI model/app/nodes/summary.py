from app.llm import model
from app.prompts.summary_prompt import summary_prompt
from app.state import CallState, Summary
from langchain_core.messages import SystemMessage


def summary_node(state: CallState) -> dict:

    structured_output = model.with_structured_output(Summary)

    response = structured_output.invoke([
        SystemMessage(content=summary_prompt),

        *state["conversation"],

        SystemMessage(
            content=f"""
Caller Information:
{state["caller_info"]}

Purpose:
{state["purpose"]}

Urgency:
{state["urgency"]}
"""
        )
    ])

    return {
        "summary": response
    }