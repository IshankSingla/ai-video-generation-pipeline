import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(topic: str) -> str:
    prompt = f"""
You are a YouTube content writer.

Write a clear, engaging narration script for a YouTube video.

Topic: {topic}

Rules:
- Length: about 60–90 seconds
- Simple spoken English
- Friendly and informative tone
- No emojis
- No bullet points
- No headings
- Just plain narration text
- End with a short concluding line

Script:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    topic = "How AI is changing education"
    script = generate_script(topic)
    print(script)
