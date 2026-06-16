import asyncio

from app.services.vision_service import get_image_description
from app.services.prompt_service import generate_internal_prompts
from app.services.variation_engine import build_variation_prompts
from app.services.similarity_engine import apply_similarity_control
from app.services.fal_service import generate_image


async def run_generation(image_url: str, strength: float = 0.7):

    # 1. UNDERSTAND IMAGE
    caption = get_image_description(image_url)

    # 2. GENERATE PROMPTS
    groq_output = generate_internal_prompts(caption)

    # 3. BUILD VARIATIONS
    prompts = build_variation_prompts(groq_output)

    # 4. APPLY SIMILARITY CONTROL
    final_prompts = [
        apply_similarity_control(p, strength)
        for p in prompts
    ]

    # 5. PARALLEL GENERATION
    loop = asyncio.get_event_loop()

    tasks = [
        loop.run_in_executor(None, generate_image, image_url, p)
        for p in final_prompts
    ]

    results = await asyncio.gather(*tasks)

    return {
        "caption": caption,
        "results": results
    }