from fastapi import APIRouter

from pydantic import BaseModel

from app.services.prompt_service import generate_prompt


router = APIRouter(
    prefix="/prompt",
    tags=["Prompt"],
)


class PromptRequest(BaseModel):

    source: str

    reference: str

    instruction: str


@router.post("/")

def create_prompt(request: PromptRequest):

    prompt = generate_prompt(

        request.source,

        request.reference,

        request.instruction,

    )

    return {

        "success": True,

        "prompt": prompt,

    }