import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def generate_internal_prompts(image_caption: str):
    """
    Turns image understanding → 4 smart variations
    """

    system = """
    You are an AI creative director.

    Convert image description into 4 transformation prompts:

    RULES:
    - keep subject same
    - change style, lighting, environment
    - do NOT ask user input

    Return JSON:
    {
      "style_variants": [
        {"type": "cinematic", "prompt": ""},
        {"type": "realistic", "prompt": ""},
        {"type": "artistic", "prompt": ""},
        {"type": "fantasy", "prompt": ""}
      ]
    }
    """

    res = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": image_caption}
            ],
            "temperature": 0.9
        }
    )

    return res.json()["choices"][0]["message"]["content"]