from app.llm import model

user_input = """
Hello, my name is Rahul Sharma. I am Vivek's colleague from ABC Technologies.
I work as a software developer. I am calling regarding the client project
that Vivek is working on.

The client has changed the requirements and we need to discuss the changes
with Vivek. Please ask Vivek to call me as soon as possible.

This is quite urgent because the client meeting is scheduled in 30 minutes
and we need to finalize the changes before the meeting.

My phone number is 9876543210. Please tell Vivek that Rahul called regarding
the client project and needs an immediate callback.
"""

response = model.invoke(user_input)

print("\n========== AI RESPONSE ==========\n")
print(response.content)