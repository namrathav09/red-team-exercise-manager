import os
import time
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create client
client = Groq(api_key=api_key)

def call_groq(prompt):
    for attempt in range(3):  # retry 3 times
        try:
            print(f"Attempt {attempt+1}...")

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            return response.choices[0].message.content

        except Exception as e:
            print("Error:", e)
            time.sleep(2)

    return "AI failed after 3 attempts"