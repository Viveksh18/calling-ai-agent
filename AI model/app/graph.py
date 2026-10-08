from langgraph.graph import StateGraph, START, END

from app.state import CallState, UrgencyLevel

from app.nodes.greeting import greeting_node
from app.nodes.caller_info import caller_info_node
from app.nodes.purpose import purpose_node
from app.nodes.urgency import urgency_node
from app.nodes.critical_urgency_node import critical_urgency_node
from app.nodes.summary import summary_node


def check_urgency(state: CallState):

    if state["urgency"].level == UrgencyLevel.CRITICAL:
        return "critical"

    return "normal"


graph_builder = StateGraph(CallState)

# Add nodes
graph_builder.add_node("greeting", greeting_node)
graph_builder.add_node("caller_info", caller_info_node)
graph_builder.add_node("purpose", purpose_node)
graph_builder.add_node("urgency", urgency_node)
graph_builder.add_node("critical", critical_urgency_node)
graph_builder.add_node("summary", summary_node)


# Connect nodes
graph_builder.add_edge(START, "greeting")

graph_builder.add_edge("greeting", "caller_info")

graph_builder.add_edge("caller_info", "purpose")

graph_builder.add_edge("purpose", "urgency")


# Conditional connection
graph_builder.add_conditional_edges(
    "urgency",
    check_urgency,
    {
        "critical": "critical",
        "normal": "summary"
    }
)

# Critical → Summary
graph_builder.add_edge("critical", "summary")

# Summary → END
graph_builder.add_edge("summary", END)


graph = graph_builder.compile()