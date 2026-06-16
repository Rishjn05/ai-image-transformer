# app/services/fal_service.py

import os
import requests
import time

FAL_KEY = os.getenv("FAL_KEY")


def generate_image(image_url: str, prompt: str, retries=2):
    url = "https://fal.run/fal-ai/flux/dev"

    payload = {
        "prompt": prompt,
        "image_url": image_url,
        "strength": 0.75
    }

    for attempt in range(retries):
        try:
            res = requests.post(
                url,
                headers={
                    "Authorization": f"Key {FAL_KEY}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=60
            )

            return res.json()

        except Exception as e:
            if attempt == retries - 1:
                return {"error": str(e)}

            time.sleep(2)