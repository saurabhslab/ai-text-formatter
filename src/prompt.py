# src/prompt.py
from langchain_core.prompts import ChatPromptTemplate

formatter_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI text formatter."),
    ("human", "Convert the following messy text into a clean, structured format:\n\n{text}")
])
