from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import uuid
import os

router = APIRouter(tags=["Generation"])

UPLOAD_FOLDER = "app/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.post("/generate")
async def generate(

    source_image: UploadFile = File(...),

    reference_image: UploadFile = File(...),

    instruction: str = Form("")

):

    source_name = f"{uuid.uuid4()}_{source_image.filename}"

    reference_name = f"{uuid.uuid4()}_{reference_image.filename}"

    source_path = os.path.join(
        UPLOAD_FOLDER,
        source_name
    )

    reference_path = os.path.join(
        UPLOAD_FOLDER,
        reference_name
    )

    with open(source_path, "wb") as f:

        f.write(await source_image.read())

    with open(reference_path, "wb") as f:

        f.write(await reference_image.read())

    return {

        "success": True,

        "instruction": instruction,

        "source": source_name,

        "reference": reference_name

    }