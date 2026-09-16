import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


class CropExplainerBot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.system_prompt = (
            "You are a farming assistant. Explain crop processes simply. "
            "Only answer questions about sowing, irrigation, harvesting, and storage."
        )

    def ask(self, user_question):
        full_message = self.system_prompt + "\n\nUser question: " + user_question

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

        response = requests.post(
            url,
            headers={
                "x-goog-api-key": self.api_key,
                "Content-Type": "application/json"
            },
            json={"contents": [{"parts": [{"text": full_message}]}]}
        )

        data = response.json()
        answer = data["candidates"][0]["content"]["parts"][0]["text"]
        return answer


bot = CropExplainerBot(api_key)
result = bot.ask("When should I water wheat?")
print(result)