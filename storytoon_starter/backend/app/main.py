from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.series import router as series_router
from app.api.characters import router as characters_router
from app.api.episodes import router as episodes_router
from app.core.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StoryToon Studio API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def healthcheck() -> dict:
    return {"status": "ok", "service": "storytoon-api"}

app.include_router(series_router, prefix="/series", tags=["series"])
app.include_router(characters_router, prefix="/characters", tags=["characters"])
app.include_router(episodes_router, prefix="/episodes", tags=["episodes"])
