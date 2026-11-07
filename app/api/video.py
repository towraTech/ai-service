from fastapi import APIRouter


router = APIRouter(
    prefix="/api/video",
    tags=["Video"],
)


@router.post("/generate")
async def generate_video():

    return {
        "success": True,
        "status": "processing",
        "message": "Video generation started",
    }