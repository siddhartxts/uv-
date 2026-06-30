import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("DEEPSEEK_API_KEY")
if not api_key:
    raise SystemExit("Missing DEEPSEEK_API_KEY — add it to your .env file (see .env.example).")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

SYSTEM_PROMPT = (
    "You are an expert social media manager who writes viral, highly engaging "
    "posts for X. Write a concise, impactful post tailored to the topic. "
    "Avoid hashtags and limit emojis. Use line breaks and empty lines for readability."
)


def generate_x_post(topic: str) -> str:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": topic},
        ],
    )
    return response.choices[0].message.content


def main():
    topic = input("What should the post be about? ")
    print(generate_x_post(topic))


if __name__ == "__main__":
    main()
