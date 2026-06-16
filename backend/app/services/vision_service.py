import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")

def get_image_description(image_url: str):
    """
    Converts image → text understanding
    """

    api_url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

    response = requests.post(
        api_url,
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": image_url}
    )

    caption = response.json()[0]["generated_text"]

    return caption