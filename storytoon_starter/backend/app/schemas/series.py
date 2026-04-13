from pydantic import BaseModel


class SeriesCreate(BaseModel):
    title: str
    description: str | None = None
    visual_style: str = "cartoon 2D"
    audience: str = "infantil"
    language: str = "pt-BR"


class SeriesOut(SeriesCreate):
    id: int

    class Config:
        from_attributes = True
