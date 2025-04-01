📚 AI Study Assistant

An intelligent, subject-wise study assistant built with **LangChain** + **OpenAI** + **Streamlit**, designed to help students learn and revise effectively by chatting with AI-powered tutors in English, Math, Science, and Social Studies.

---

🎯 Features

- Subject-wise tutor (English, Math, Science, Social Studies)
- Memory-enabled conversations
- Streamlit chat interface
- OpenAI GPT-based responses
- Modular backend using LangChain

---

🧰 Tech Stack

- **LangChain**
- **OpenAI GPT (via langchain-openai)**
- **Streamlit** (Frontend)
- **Python 3.10+**
- **.env for API security**

---

🛠️ Installation

```bash
git clone https://github.com/T-ABISHEK/AI-Study-Assistant.git
cd AI-Study-Assistant
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (on Windows)
pip install -r requirements.txt
```

---

🔐 Setup

Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> `.env` is ignored in Git using `.gitignore`

---

🚀 Run the App

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---
