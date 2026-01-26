from typing import Optional
from pydantic import BaseModel
from datetime import datetime




class StoryJobBase(BaseModel):
    theme: str

class StoryJobResponse(BaseModel):
    job_id: int
    status: str
    created_at: datetime
    story_id: Optional[int] = None
    completed_at: Optonal[datetime] = None
    error: Optional[str] = None

    class Config:
        form_attributes = True


class StoryJobCreate(StoryJobBase):
    pass