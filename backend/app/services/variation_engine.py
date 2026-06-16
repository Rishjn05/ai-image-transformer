import json

def build_variation_prompts(groq_output: str):
    data = json.loads(groq_output)

    return [
        item["prompt"]
        for item in data["style_variants"]
    ]