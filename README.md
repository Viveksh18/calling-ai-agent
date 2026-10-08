# 🤖 AI Calling Assistant

An intelligent, modular **AI Calling Assistant** built with **Python, LangChain, LangGraph, Pydantic, and Groq LLMs**.

The system is designed to understand incoming caller conversations, extract important caller information, identify the purpose of the call, determine its urgency, trigger actions for critical calls, and generate a concise call summary.

> 🚧 **Project Status:** Active Development

---

## 📌 Overview

The AI Calling Assistant acts as an intelligent first-level call handler.

Instead of manually processing every incoming call, the system can analyze a conversation and determine:

* 👋 How to greet the caller
* 👤 Who the caller is
* 📞 How the caller is related to the user
* 💼 What the caller does
* 🎯 Why the caller is calling
* 📝 What action the caller is requesting
* 🚨 How urgent the call is
* ⚡ Whether immediate action is required
* 📋 A concise summary of the conversation

The project uses **LangGraph** to represent the call-handling process as a stateful workflow.

---

# ✨ Key Features

### 👋 Intelligent Greeting

Generates an appropriate and professional greeting for incoming callers.

### 👤 Caller Information Extraction

Extracts structured information such as:

* Name
* Relationship
* Phone number
* Work/profession

### 🎯 Purpose Detection

Identifies:

* Purpose category
* Main purpose
* Caller request
* Requested action
* Important details

### 🚨 Urgency Detection

Classifies calls into:

```text
LOW
NORMAL
MEDIUM
HIGH
CRITICAL
```

The system also provides a reason for the assigned urgency level.

### ⚡ Critical Call Handling

If a call is classified as `CRITICAL`, LangGraph routes the workflow through a dedicated critical-action node.

Future actions can include:

* SMS notification
* WhatsApp notification
* Email notification
* Push notification
* Automatic callback
* Emergency escalation

### 📋 Automatic Call Summary

After processing the conversation, the system generates a structured summary containing the most important information.

### 🧩 Modular Architecture

The project separates:

* LLM configuration
* State management
* Prompts
* Nodes
* Graph workflow
* Testing

This makes the project easier to maintain and extend.

---

# 🏗️ System Architecture

```text
                    ┌───────────────┐
                    │ Incoming Call │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │    Greeting   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌────────────────┐
                    │  Caller Info   │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │     Purpose    │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │    Urgency     │
                    └───────┬────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
              CRITICAL              NORMAL
                 │                     │
                 ▼                     │
        ┌─────────────────┐             │
        │ Critical Action │             │
        └────────┬────────┘             │
                 │                     │
                 └──────────┬──────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │     Summary    │
                    └───────┬────────┘
                            │
                            ▼
                           END
```

---

# 🧠 LangGraph Workflow

The workflow is implemented using a `CallState` object.

```text
START
  ↓
Greeting
  ↓
Caller Information
  ↓
Purpose
  ↓
Urgency
  ↓
Conditional Routing
  ├── CRITICAL → Critical Action
  │                    ↓
  │                 Summary
  │
  └── NORMAL ─────→ Summary
                       ↓
                      END
```

This architecture allows additional nodes and conditional paths to be added without rewriting the entire application.

---

# 📦 Technology Stack

| Technology        | Purpose                               |
| ----------------- | ------------------------------------- |
| **Python**        | Core programming language             |
| **LangChain**     | LLM integration and structured output |
| **LangGraph**     | Stateful AI workflow orchestration    |
| **Pydantic**      | Structured data validation            |
| **Groq**          | LLM API                               |
| **GPT-OSS-20B**   | Current LLM used for testing          |
| **python-dotenv** | Environment variable management       |
| **PowerShell**    | Development environment               |
| **Git/GitHub**    | Version control and collaboration     |

---

# 📁 Project Structure

```text
AI model/
│
├── app/
│   ├── __init__.py
│   │
│   ├── llm.py
│   ├── state.py
│   ├── graph.py
│   │
│   ├── nodes/
│   │   ├── __init__.py
│   │   ├── greeting.py
│   │   ├── caller_info.py
│   │   ├── purpose.py
│   │   ├── urgency.py
│   │   ├── critical.py
│   │   └── summary.py
│   │
│   └── prompts/
│       ├── __init__.py
│       ├── greeting_prompt.py
│       ├── caller_info_prompt.py
│       ├── purpose_prompt.py
│       ├── urgency_prompt.py
│       └── summary_prompt.py
│
├── test/
│   ├── __init__.py
│   └── test_llm.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🔄 Data Flow

The system maintains a shared state throughout the workflow.

Example:

```python
CallState = {
    "conversation": [...],
    "greeting": "...",
    "caller_info": ...,
    "purpose": ...,
    "urgency": ...,
    "summary": ...
}
```

Each node reads the required information from the state and returns only the fields it updates.

For example:

```python
return {
    "caller_info": response
}
```

The next node can then access:

```python
state["caller_info"]
```

This allows information to flow cleanly between LangGraph nodes.

---

# 🧱 State Models

The project uses Pydantic models for structured information.

### Caller Information

```python
class Caller_info(BaseModel):
    name: str
    relationship: str
    phone: str
    work: str
```

### Purpose

```python
class Purpose(BaseModel):
    purpose_category: str
    main_purpose: str
    caller_request: str
    requested_action: str
    important_details: Optional[str] = None
```

### Urgency

```python
class Urgency(BaseModel):
    level: UrgencyLevel
    reason: str
```

### Summary

```python
class Summary(BaseModel):
    summary: str
```

---

# 🧠 LLM Configuration

The LLM configuration is centralized in:

```text
app/llm.py
```

Example:

```python
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)
```

Nodes import the shared model:

```python
from app.llm import model
```

This prevents the model configuration from being duplicated throughout the application.

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### ⚠️ Security

Never commit your `.env` file to GitHub.

Add it to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If an API key is accidentally exposed, revoke it immediately and generate a new one.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

```bash
cd YOUR_REPOSITORY
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 🧪 Testing the LLM

The project includes:

```text
test/test_llm.py
```

Run it from the project root:

```powershell
python -m test.test_llm
```

Example test conversation:

```text
Hello, my name is Rahul Sharma. I am Vivek's colleague
from ABC Technologies.

I work as a software developer. I am calling regarding
the client project.

The client has changed the requirements and we need to
discuss the changes with Vivek.

Please ask Vivek to call me as soon as possible.

The client meeting is scheduled in 30 minutes, so this
is quite urgent.

My phone number is 9876543210.
```

The LLM should understand the context and generate an appropriate response.

---

# 📊 Example Expected Extraction

### Caller Information

```text
Name: Rahul Sharma
Relationship: Colleague
Phone: 9876543210
Work: Software Developer
```

### Purpose

```text
Category: Client Project
Purpose: Discuss changed project requirements
Requested Action: Ask Vivek to call Rahul
```

### Urgency

```text
Level: CRITICAL

Reason:
The client meeting is scheduled in 30 minutes.
```

### Summary

```text
Rahul Sharma from ABC Technologies called regarding
changes to the client project requirements. He needs
Vivek to call him immediately because the client meeting
is scheduled in 30 minutes.
```

---

# 🧩 Structured LLM Output

Instead of relying only on free-form text, the project uses LangChain's structured output capabilities.

Example:

```python
structured_output = model.with_structured_output(Caller_info)

response = structured_output.invoke([
    SystemMessage(content=caller_info_prompt),
    *state["conversation"]
])
```

This allows the model output to be validated against a Pydantic schema.

---

# 🚨 Conditional Urgency Routing

The system checks the urgency level after the urgency node.

```python
def check_urgency(state: CallState):

    if state["urgency"].level == UrgencyLevel.CRITICAL:
        return "critical"

    return "normal"
```

LangGraph then routes the call:

```text
Urgency
   │
   ├── CRITICAL → Critical Action
   │
   └── Other → Summary
```

This is one of the main advantages of using LangGraph instead of a simple sequential LLM chain.

---

# 🎯 Current Project Goals

The project is being developed toward a complete AI-based calling assistant capable of:

* [x] LLM integration
* [x] Shared LLM configuration
* [x] LangGraph workflow
* [x] Caller information extraction
* [x] Purpose extraction
* [x] Urgency classification
* [x] Conditional critical-call routing
* [x] Call summarization
* [ ] Real-time voice input
* [ ] Speech-to-text
* [ ] Text-to-speech
* [ ] Telephony integration
* [ ] Real-time conversation state
* [ ] Caller identification
* [ ] Notification system
* [ ] Call history
* [ ] Database integration
* [ ] Authentication
* [ ] Production deployment

---

# 🚀 Future Architecture

The long-term system can evolve into:

```text
                    Phone Call
                        │
                        ▼
                 Speech-to-Text
                        │
                        ▼
                 Conversation
                        │
                        ▼
                ┌──────────────┐
                │  LangGraph   │
                │    Agent     │
                └──────┬───────┘
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
   Caller Info      Purpose          Urgency
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                    Summary
                       │
                       ▼
                 Action Router
                       │
        ┌──────────────┼───────────────┐
        ▼              ▼               ▼
       SMS          WhatsApp          Email
        │              │               │
        └──────────────┴───────────────┘
                       │
                       ▼
                  Text-to-Speech
                       │
                       ▼
                    Caller
```

---

# 🔮 Planned Integrations

Future versions may integrate:

### 📞 Telephony

* Twilio
* SIP
* VoIP services
* Phone call APIs

### 🎙️ Speech

* Speech-to-text
* Text-to-speech
* Real-time audio streaming

### 📩 Notifications

* SMS
* WhatsApp
* Email
* Push notifications

### 🗄️ Database

Potential storage:

```text
Users
Calls
Callers
Conversations
Summaries
Actions
Notifications
```

---

# 👥 Team Development

For a two-person development team, the project can be divided into:

### Developer 1 — AI/Backend

Responsible for:

* LangGraph
* LangChain
* LLM integration
* Prompt engineering
* State management
* Caller analysis
* Urgency detection
* Backend APIs

### Developer 2 — Application/Integration

Responsible for:

* Frontend
* Voice interface
* Telephony integration
* Database
* Authentication
* Notifications
* Deployment

Both developers should work with Git branches and pull requests rather than directly modifying the same branch.

Example:

```text
main
 │
 ├── feature/langgraph
 │
 ├── feature/voice
 │
 ├── feature/database
 │
 └── feature/frontend
```

---

# 📈 Development Roadmap

| Phase | Feature                       | Status |
| ----- | ----------------------------- | ------ |
| 1     | Python project setup          | ✅      |
| 2     | LLM API integration           | ✅      |
| 3     | LangChain integration         | ✅      |
| 4     | Pydantic state models         | ✅      |
| 5     | LangGraph workflow            | ✅      |
| 6     | Caller information extraction | ✅      |
| 7     | Purpose detection             | ✅      |
| 8     | Urgency classification        | ✅      |
| 9     | Critical-call routing         | ✅      |
| 10    | Call summarization            | ✅      |
| 11    | Speech-to-text                | 🔲     |
| 12    | Text-to-speech                | 🔲     |
| 13    | Telephony integration         | 🔲     |
| 14    | Notification system           | 🔲     |
| 15    | Database                      | 🔲     |
| 16    | Web dashboard                 | 🔲     |
| 17    | Production deployment         | 🔲     |

---

# 🛡️ Security Considerations

Because the system processes potentially sensitive call information:

* Never expose API keys.
* Never commit `.env`.
* Validate structured LLM output.
* Sanitize user input.
* Implement authentication before production deployment.
* Encrypt sensitive stored data.
* Apply appropriate access controls.
* Maintain logs without unnecessarily storing sensitive information.
* Follow applicable privacy and telecommunications regulations.

---

# ⚠️ Current Limitations

This project is currently a development prototype.

At the current stage:

* The system processes provided conversation text rather than a live phone call.
* Voice recognition is not yet integrated.
* Telephony integration is not yet implemented.
* Critical actions are currently represented by workflow nodes rather than production notification services.
* Persistent conversation storage is not yet implemented.

---

# 🤝 Contributing

Contributions are welcome.

### 1. Fork the repository

```bash
git fork
```

### 2. Create a feature branch

```bash
git checkout -b feature/your-feature
```

### 3. Commit your changes

```bash
git add .
git commit -m "Add your feature"
```

### 4. Push the branch

```bash
git push origin feature/your-feature
```

### 5. Open a Pull Request

Please describe:

* What was changed
* Why it was changed
* How it was tested
* Any future improvements required

---

# 📄 License

This project is currently intended for learning and development purposes.

Add an appropriate open-source license before distributing the project publicly.

For example:

```text
MIT License
```

---

# 👨‍💻 Author

**Vivek Sharma**

AI Developer | AI Agent Development | Python | LangChain | LangGraph

---

# ⭐ Project Vision

The goal of this project is to evolve from a basic LLM-powered call analyzer into a **fully autonomous AI Calling Assistant** capable of answering calls, understanding conversations, making decisions, taking appropriate actions, and keeping the user informed without requiring manual intervention.

```text
Listen → Understand → Decide → Act → Summarize
```

---

## 🚀 Status

**Currently in active development.**

More capabilities will be added as the project progresses toward real-time voice and telephony integration.
