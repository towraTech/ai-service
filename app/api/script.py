from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.ai_service import AIService


router = APIRouter(
    prefix="/api/script",
    tags=["Script"],
)


ai_service = AIService()


class ScriptRequest(BaseModel):

    script: str


@router.post("/analyze")
async def analyze_script(
    request: ScriptRequest
):

    if not request.script.strip():

        raise HTTPException(
            status_code=400,
            detail="Script is required",
        )

    try:

        result = await ai_service.analyze_script(
            request.script
        )

        return {
            "success": True,
            "data": result,
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(error)}",
        )