from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.models import Character
from app.schemas.character import CharacterCreate, CharacterOut

router = APIRouter()


@router.get("", response_model=list[CharacterOut])
def list_characters(db: Session = Depends(get_db)):
    return db.query(Character).order_by(Character.id.desc()).all()


@router.post("", response_model=CharacterOut)
def create_character(payload: CharacterCreate, db: Session = Depends(get_db)):
    item = Character(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
