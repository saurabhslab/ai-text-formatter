# AI Text Formatter

AI Text Formatter is a Python project that converts messy, unstructured text into clean, readable, and well-structured formats using **Google Gemini API** and **LangChain v1 (Runnable interface)**.

---

## 🚀 Features

- Converts messy text into structured output
- Clean, minimal project structure

---

## 🧰 Tech Stack

- Python 3.9+
- LangChain v1
- Google Gemini API
- `langchain-google-genai`
- `python-dotenv`

---
⚙️ Setup Instructions
1️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

2️⃣ Install dependencies
pip install --upgrade langchain langchain-google-genai python-dotenv

3️⃣ Configure Gemini API key

▶️ Run the Formatter
python src/formatter.py


Example output:

Input:
this is messy text no structure bullets missing

Output:
- This is messy text
- No structure
- Bullets were missing


  

