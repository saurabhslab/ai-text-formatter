from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from prompt import formatter_prompt
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.7
)

chain = formatter_prompt | llm

def format_text(messy_text: str) -> str:
    response = chain.invoke({"text": messy_text})
    return response.content


if __name__ == "__main__":
    messy = "this is messy text no headings bullets missing"
    print(format_text(messy))
