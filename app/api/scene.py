from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.image_service import ImageService


router = APIRouter(
    prefix="/api/scene",
    tags=["Scene"]
)


image_service = ImageService()


class SceneImageRequest(BaseModel):

    scene_number: int

    visual_prompt: str


@router.post("/generate-image")
async def generate_scene_image(
    request: SceneImageRequest
):

    if not request.visual_prompt.strip():

        raise HTTPException(
            status_code=400,
            detail="Visual prompt is required"
        )

    try:

        result = image_service.generate_image(
            request.visual_prompt,
            output_dir="outputs/scenes"
        )

        return {
            "success": True,
            "scene_number": request.scene_number,
            "image": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )