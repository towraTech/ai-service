import os
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.audio_service import AudioService


router = APIRouter(
    prefix="/api/audio",
    tags=["Audio"]
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


audio_service = AudioService()


ALLOWED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".m4a",
    ".mp4",
    ".webm",
    ".ogg"
}


@router.post("/upload")
async def upload_audio(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Audio file is required"
        )

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported audio format. "
                "Supported formats: "
                "mp3, wav, m4a, mp4, webm, ogg"
            )
        )

    file_id = str(uuid.uuid4())

    filename = f"{file_id}{extension}"

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    try:

        content = await file.read()

        with open(file_path, "wb") as buffer:
            buffer.write(content)

        transcription = audio_service.transcribe(
            file_path
        )

        return {
            "success": True,
            "file_id": file_id,
            "filename": file.filename,
            "transcription": transcription
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Audio processing failed: {str(error)}"
        )