from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.db import Base


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    visual_style = Column(String(120), nullable=False, default="cartoon 2D")
    audience = Column(String(80), nullable=False, default="infantil")
    language = Column(String(40), nullable=False, default="pt-BR")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, ForeignKey("series.id"), nullable=False)
    name = Column(String(120), nullable=False)
    role = Column(String(80), nullable=False, default="protagonista")
    description = Column(Text, nullable=False)
    canonical_look = Column(Text, nullable=False)
    voice_id = Column(String(120), nullable=False, default="voz_padrao")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Episode(Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    series_id = Column(Integer, ForeignKey("series.id"), nullable=False)
    title = Column(String(200), nullable=False)
    story_text = Column(Text, nullable=False)
    target_duration_minutes = Column(Integer, nullable=False, default=10)
    status = Column(String(40), nullable=False, default="draft")
    outline_json = Column(Text, nullable=True)
    final_video_url = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
