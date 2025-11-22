import google.generativeai as genai
from .config import API_KEY, MODEL_NAME
from .tools import calculate_tax_compliance, fuzzy_match_vendor

def _configure_api() -> None:
    """Configure the Gemini API with the API key."""
    if not API_KEY:
        raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")
    genai.configure(api_key=API_KEY)

class AnalystAgent:
    def __init__(self):
        _configure_api()
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            tools=[calculate_tax_compliance, fuzzy_match_vendor]
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def analyze(self, prompt: str):
        """Analyze the given prompt using the LLM."""
        return self.chat.send_message(prompt)
    
    def inject_message(self, message: str):
        """Inject a message into the chat history."""
        return self.chat.send_message(message)
