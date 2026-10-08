from app.graph import graph
from langchain_core.messages import HumanMessage


conversation = [
    HumanMessage(
        content=(
            "Hello, my name is Ankit Verma. "
            "I am a customer of TechNova Solutions."
        )
    ),

    HumanMessage(
        content=(
            "I work as a business owner and I am calling "
            "because our payment system is not working."
        )
    ),

    HumanMessage(
        content=(
            "Our customers are unable to complete payments "
            "on our website, and we are losing orders."
        )
    ),

    HumanMessage(
        content=(
            "Please ask Vivek to contact me immediately. "
            "We have many customers waiting and this issue "
            "needs to be fixed as soon as possible."
        )
    ),

    HumanMessage(
        content=(
            "My phone number is 9123456780."
        )
    ),
]


initial_state = {
    "conversation": conversation,
    "greeting": "",
    "caller_info": None,
    "purpose": None,
    "urgency": None,
    "summary": None,
}


result = graph.invoke(initial_state)


print("\n========== CALL RESULT ==========\n")

print("Greeting:")
print(result["greeting"])

print("\nCaller Information:")
print(result["caller_info"])

print("\nPurpose:")
print(result["purpose"])

print("\nUrgency:")
print(result["urgency"])

print("\nSummary:")
print(result["summary"])

print("\n=================================")