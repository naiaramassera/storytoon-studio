import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.models import Episode, Character
from app.schemas.episode import EpisodeCreate, EpisodeOut
from app.services.script_engine import build_episode_outline
from app.workers.tasks import start_episode_pipeline

router = APIRouter()


@router.get("", response_model=list[EpisodeOut])
def list_episodes(db: Session = Depends(get_db)):
    return db.query(Episode).order_by(Episode.id.desc()).all()


@router.post("", response_model=EpisodeOut)
def create_episode(payload: EpisodeCreate, db: Session = Depends(get_db)):
    item = Episode(**payload.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.post("/{episode_id}/build-outline")
def generate_outline(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")

    characters = db.query(Character).filter(Character.series_id == episode.series_id).all()
    outline = build_episode_outline(
        title=episode.title,
        story_text=episode.story_text,
        target_duration_minutes=episode.target_duration_minutes,
        characters=characters,
    )
    episode.outline_json = json.dumps(outline, ensure_ascii=False, indent=2)
    episode.status = "outlined"
    db.commit()
    return {"status": "outlined", "outline": outline}


@router.post("/{episode_id}/render")
def render_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.id == episode_id).first()
    if not episode:
        raise HTTPException(status_code=404, detail="Episódio não encontrado")
    episode.status = "queued"
    db.commit()
    start_episode_pipeline.delay(episode_id)
    return {"status": "queued", "episode_id": episode_id}
