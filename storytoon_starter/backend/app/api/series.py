from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.models import Series
from app.schemas.series import SeriesCreate, SeriesOut

router = APIRouter()


@router.get("", response_model=list[SeriesOut])
def list_series(db: Session = Depends(get_db)):
    return db.query(Series).order_by(Series.id.desc()).all()


@router.post("", response_model=SeriesOut)
def create_series(payload: SeriesCreate, db: Session = Depends(get_db)):
    item = Series(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
