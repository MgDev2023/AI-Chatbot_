# AI Chatbot

A simple AI chatbot that answers any question you type.

---

## What does it do?

You type a question, it gives you an answer. It uses the Llama 3.1 language model through the Groq API — which is fast and free to use.

The UI is built with Streamlit so it looks like a proper chat interface.

---

## Tech used

- Python
- Groq API (Llama 3.1 model)
- Streamlit (chat interface)

---

## How to run it locally

```bash
git clone https://github.com/MgDev2023/AI-Chatbot_.git
cd AI-Chatbot_
pip install -r requirements.txt
```

Create a `.env` file with your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

Then run:
```bash
streamlit run AI_Chatbot/chatbot.py
```

---

## Files

```
AI-Chatbot_/
└── AI_Chatbot/
    ├── chatbot.py       ← main app
    └── requirements.txt
```

---

## Made by

Megan — small project to learn how to connect to LLM APIs and build a chat interface.
