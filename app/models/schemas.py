from pydantic import BaseModel
from typing import List, Optional


class Scene(BaseModel):

    scene_number: int

    start_time: float

    end_time: float

    duration: float

    narration: str

    description: str

    visual_prompt: str

    mood: Optional[str] = None

    camera: Optional[str] = None

    location: Optional[str] = None


class SceneResponse(BaseModel):

    scenes: List[Scene]