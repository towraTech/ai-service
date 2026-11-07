from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.audio import router as audio_router
from app.api.script import router as script_router
from app.api.video import router as video_router
from app.api.image import router as image_router


app = FastAPI(
    title="AI Video Creator API",
    description="AI Video Creation and Audio to Video Service",
    version="1.0.0",
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# API ROUTES
# =========================================================

app.include_router(audio_router)
app.include_router(script_router)
app.include_router(video_router)
app.include_router(image_router)

# =========================================================
# ROOT
# =========================================================

@app.get("/")
async def root():
    return {
        "application": "AI Video Creator",
        "status": "running",
        "version": "1.0.0",
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "ai-video-service",
    }