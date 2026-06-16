from fastapi import APIRouter
from pydantic import BaseModel

from app.services.image_service import run_generation

router = APIRouter()


class Request(BaseModel):
    image_url: str
    strength: float = 0.7


@router.post("/generate")
async def generate(req: Request):

    output = await run_generation(
        req.image_url,
        req.strength
    )

    return {
        "success": True,
        "caption": output["caption"],
        "images": output["results"]
    }