from app.llm import model
from app.state import CallState, Urgency, UrgencyLevel
from app.prompts import urgency_prompt
from langchain.messages import SystemMessage



def critical_urgency_node(state: CallState) -> dict:

    urgency = state["urgency"]

    print("🚨 CRITICAL CALL")
    print(f"Reason: {urgency.reason}")

    # Later you can:
    # - send SMS
    # - send WhatsApp notification
    # - send email
    # - make another call
    # - trigger an emergency workflow

    return {}