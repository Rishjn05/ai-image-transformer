from groq import Groq

from app.config import GROQ_API_KEY


client = Groq(
    api_key=GROQ_API_KEY
)


SYSTEM_PROMPT = """
You are an expert AI Image Prompt Engineer.

Rules:

1. Preserve the uploaded object.
2. Merge style from reference.
3. Follow user instruction.
4. Produce one high quality FLUX prompt.

Return only the final prompt.
"""


def generate_prompt(
    source_description: str,
    reference_description: str,
    instruction: str,
):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.5,

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },

            {
                "role": "user",
                "content": f"""

Source Image

{source_description}

Reference Style

{reference_description}

User Instruction

{instruction}

Generate one detailed prompt.

""",
            },

        ],

    )

    return response.choices[0].message.content