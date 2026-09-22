from google import genai
from google.genai import types
import os

# Put your NEW API key in an environment variable.
API_KEY = os.getenv("AQ.Ab8RN6LdQCrUL1PRPaxFddkVwfKWIDaRItWJumwcTHcQj1QBhw")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set.")

client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
You are Vennela, a helpful AI assistant.

Response rules:
- Give accurate, useful answers.
- Understand the user's question before answering.
- Do not invent facts. If you are uncertain, say so.
- Prefer concise answers unless the user asks for detail.
- Use clear, natural conversational language.
- Follow the user's instructions carefully.
- For calculations, reason carefully and verify the result.
- If the question is ambiguous, ask a short clarification.
- Do not repeat the user's question unnecessarily.
- make the multiple steps to get the exact output.
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello Vennela",
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.2,
            top_p=0.9,
            max_output_tokens=2048,
        ),
    )

    print(response.text)

except Exception as e:
    print(f"Gemini API error: {e}")