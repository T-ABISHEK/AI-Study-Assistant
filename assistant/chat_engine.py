from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from assistant.prompt_manager import get_prompt
from assistant.memory import get_memory
import os

def get_chat_chain(subject: str):
    prompt_template = get_prompt(subject)
    prompt = ChatPromptTemplate.from_template(f"""
    {{history}}
    Student: {{input}}
    AI ({subject} Expert):
    """)

    llm = ChatOpenAI(temperature=0.5, api_key=os.getenv("OPENAI_API_KEY"))
    memory = get_memory()
    return ConversationChain(llm=llm, prompt=prompt, memory=memory, verbose=False)