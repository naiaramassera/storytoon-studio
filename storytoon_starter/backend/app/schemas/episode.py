from pydantic import BaseModel


class EpisodeCreate(BaseModel):
    series_id: int
    title: str
    story_text: str
    target_duration_minutes: int = 10


class EpisodeOut(EpisodeCreate):
    id: int
    status: str
    outline_json: str | None = None
    final_video_url: str | None = None

    class Config:
        from_attributes = True
