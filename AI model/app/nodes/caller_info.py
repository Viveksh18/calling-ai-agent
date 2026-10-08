from app.llm import model
from app.prompts.call_info_prompt import caller_info_prompt
from app.state import CallState, Caller_info
from langchain_core.messages import SystemMessage


def caller_info_node(state: CallState) -> dict:

    structure_output = model.with_structured_output(Caller_info)

    response = structure_output.invoke([SystemMessage(content=caller_info_prompt)])

    return{
        "caller_info": response
    }
