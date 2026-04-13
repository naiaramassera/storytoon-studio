from pydantic import BaseModel


class CharacterCreate(BaseModel):
    series_id: int
    name: str
    role: str = "protagonista"
    description: str
    canonical_look: str
    voice_id: str = "voz_padrao"


class CharacterOut(CharacterCreate):
    id: int

    class Config:
        from_attributes = True
