from app.graph import graph


def main():
    initial_state = {
        "conversation": [],
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


if __name__ == "__main__":
    main()