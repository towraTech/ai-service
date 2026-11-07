from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.image_service import ImageService


router = APIRouter(
    prefix="/api/image",
    tags=["Image"]
)


image_service = ImageService()


class ImageRequest(BaseModel):

    prompt: str


@router.post("/generate")
async def generate_image(
    request: ImageRequest
):

    if not request.prompt.strip():

        raise HTTPException(
            status_code=400,
            detail="Prompt is required"
        )

    try:

        result = image_service.generate_image(
            request.prompt
        )

        return result

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Image generation failed: {str(error)}"
        )